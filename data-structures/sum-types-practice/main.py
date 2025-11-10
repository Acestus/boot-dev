from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            csv_data = [
                [str(item) for item in row]
                for row in data
            ]
            return ("Pending...", csv_data)
        case CSVExportStatus.PROCESSING:
            csv_string = "\n".join(
                ",".join(str(item) for item in row)
                for row in data
            )
            return ("Processing...", csv_string)
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            csv_string = "\n".join(
                ",".join(str(item) for item in row)
                for row in data
            )
            return ("Unknown error, retrying...", csv_string)
        case _:
            raise ValueError("unknown export status")
