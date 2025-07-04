from database.DB_connect import DBConnect
from model.arco import Arco
from model.driver import Driver


class DAO():

    @staticmethod
    def getAllYear():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select distinct s.`year` as `year` 
                    from seasons s"""

        cursor.execute(query)

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select distinct d.*
                    from results r , drivers d , races r2 
                    where d.driverId = r.driverId and r.raceId = r2.raceId 
                    and r.`position`  is not null
                    and r2.`year`  = %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Driver(**row))

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getallEdges(year, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select r1.driverId as vincente, r2.driverId as perdente, count(*) as peso
                    from results r1, results r2, races r 
                    where r1.raceId = r2.raceId and r2.raceId = r.raceId 
                    and r.`year` = %s
                    and r1.`position`  < r2.`position`
                    and r1.`position` is not null and r2.`position` is not null
                    group by r1.driverId, r2.driverId"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Arco(idMap[row["vincente"]], idMap[row["perdente"]], row["peso"]))

        cursor.close()
        conn.close()
        return result
