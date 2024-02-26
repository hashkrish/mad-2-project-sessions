# get the package "celery" path


from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from celery_m import celery_app
from e2e_messenger.models import db, Report, Message, User


@celery_app.task
def add(x, y):
    from time import sleep

    sleep(20)
    return x + y


@celery_app.task
def generate_reports():
    from e2e_messenger import create_app
    from config import LocalConfig

    app = create_app()
    app.config.from_object(LocalConfig)

    app.app_context().push()
    reports = Report.query.filter_by(status="PENDING").all()

    data = [["ID", "Sender ID", "Receiver ID", "Timestamp"]]
    for message in Message.query.all():
        sender = User.query.filter_by(id=message.sender_id).first()
        receiver = User.query.filter_by(id=message.receiver_id).first()

        data.append([message.id, sender.username, receiver.username, message.timestamp])

    def generate_pdf(data, report):
        pdf_filename = "report_" + str(report.id) + ".pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=A4)
        elements = []

        # Define styles
        styles = getSampleStyleSheet()

        # Add a heading
        heading = Paragraph("Daily Report", styles["Heading1"])
        elements.append(heading)
        elements.append(Spacer(1, 12))

        table = Table(data)

        # Add style to the table
        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )

        table.setStyle(style)

        # Add the table to the elements list
        elements.append(table)

        # Build the PDF
        pdf.build(elements)

        print(f"PDF generated successfully: {pdf_filename}")

    for report in reports:
        generate_pdf(data, report)
        report.status = "COMPLETED"
        report.path = "./report_" + str(report.id) + ".pdf"
        db.session.commit()
    return True


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, generate_reports.s(), name="add every 10")

    # # Calls test('hello') every 30 seconds.
    # # It uses the same signature of previous task, an explicit name is
    # # defined to avoid this task replacing the previous one defined.
    # sender.add_periodic_task(30.0, test.s("hello"), name="add every 30")

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s("world"), expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s("Happy Mondays!"),
    # )
