import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def execute_query(self, query, params=()):
        self.cur.execute(query, params)
        return self.dict_fetchall(self.cur)

    def get_all_regions(self):
        return self.execute_query("SELECT * FROM regions")

    def get_all_jobs(self):
        return self.execute_query("SELECT * FROM jobs")

    def get_countries_by_region(self, region_id):
        return self.execute_query("SELECT * FROM countries WHERE region_id = ?", (region_id,))

    def get_employees_by_job(self, job_id):
        query = """
        SELECT employee_id, first_name, last_name
        FROM employees
        WHERE job_id = ?
        """
        employees = self.execute_query(query, (job_id,))
        return [{"employee_id": emp["employee_id"], "name": f"{emp['first_name']} {emp['last_name']}"} for emp in
                employees]

    def get_countries_by_jobs(self, job_id):
        return self.execute_query("SELECT * FROM employees WHERE job_id = ?", (job_id,))

    def dict_fetchall(self, cursor):
        columns = [i[0] for i in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

# Misol:
# db = Database("sample-database.db")
# regions = db.get_all_regions()
# print(regions)







