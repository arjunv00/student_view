import mysql.connector


class Dbconnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arjunvinayak@123",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None


class StudentManagement(Dbconnect):

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "select * from student"
            self.cursor.execute(query)

            record = self.cursor.fetchall()

            for data in record:
                print(data)

        except Exception as e:
            print(e)

    def post(self, **kwargs):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()

        query = """
                INSERT INTO student
                (name, place, mobile, email, course, fees, joining_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

        values = [v for v in kwargs.values()]

        self.cursor.execute(query, values)
        self.connect.commit()

        print("New student added successfully")

    def retrieve(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "select * from student where id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            if record == None:
                print("Student not found")

            print(record)

        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "select * from student where id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            return None

    def delete(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "delete from student where id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            if self.cursor.rowcount > 0:
                self.connect.commit()
                print("Student deleted successfully")
            else:
                print("Student not found")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:
                self.connect = super().get_connection()
                self.cursor = self.connect.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s, "

                placeholder = placeholder.rstrip(", ")

                query = f"update student set {placeholder} where id=%s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Student details updated successfully......")

            else:
                print("Student not found.....")

        except Exception as e:
            print(e)


connection_instance = Dbconnect()

print(connection_instance.get_connection())

student_instance = StudentManagement()


# POST
# student_instance.post(
#     name="Arjun",
#     place="Perumbavoor",
#     mobile="9876543210",
#     email="arjun@gmail.com",
#     course="Python",
#     fees=25000,
#     joining_date="2026-09-09"
# )


# GET ALL
# student_instance.get()


# RETRIEVE BY ID
# student_instance.retrieve(id=2)


# GET OBJECT
# print(student_instance.get_object(id=1))


# DELETE
# student_instance.delete(id=2)


# PUT
# student_instance.put(
#     id=2,
#     name="Arjun Vinayak",
#     place="Perumbavoor",
#     course="Python",
#     fees=30000
# )