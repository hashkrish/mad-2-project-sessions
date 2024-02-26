from flask_restful import Resource, reqparse, fields, marshal_with
from e2e_messenger.extensions import db
from e2e_messenger.models import Report

report_fields = {
    "id": fields.Integer,
    "status": fields.String,
    "path": fields.String,
    "timestamp": fields.String,
}


class ReportResource(Resource):
    def get(self, report_id):
        report = Report.query.filter_by(id=report_id).first()
        if report:
            return report, 200
        return {"error": "Report {} doesn't exist".format(report_id)}, 404

    @marshal_with(report_fields)
    def put(self, report_id):
        report = Report.query.filter_by(id=report_id).first()
        if report:
            args = parser.parse_args()
            for arg in args:
                if args[arg] is not None:
                    setattr(report, arg, args[arg])
            db.session.commit()
            return report, 200
        return {"error": "Report {} doesn't exist".format(report_id)}, 404


class ReportsResource(Resource):
    @marshal_with(report_fields)
    def post(self):
        report = Report()
        db.session.add(report)
        db.session.commit()
        return report, 201

    @marshal_with(report_fields)
    def get(self):
        reports = Report.query.all()
        return reports, 200
