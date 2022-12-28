class Timetracking:

    def __init__(self,
                 date: str,
                 start_time: str,
                 lunch_start: str,
                 lunch_end: str,
                 end_time: str,
                 user_id: str) -> None:

        self.start_time = f"{date} {start_time}" if start_time else ""
        self.lunch_start = f"{date} {lunch_start}" if lunch_start else ""
        self.lunch_end = f"{date} {lunch_end}" if lunch_end else ""
        self.end_time = f"{date} {end_time}" if end_time else ""
        self.user_id = user_id
