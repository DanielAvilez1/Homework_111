from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        user = {
            "id": result[0],
            "year": result[1],
            "make": result[2],
            "model": result[3],
            "active": result[4]
        }
        out.append(user)
    return out


def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=? AND active=1",
        (pk,)
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(user_dict):
    value_tuple = (
        user_dict.get("year"),
        user_dict.get("make"),
        user_dict.get("model")
    )
    statement = """
            INSERT INTO user (
                year,
                make,
                model
            ) VALUES (?,?,?)
    """

    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def update(pk, user_data):
    value_tuple = (
        vehicle_data.get("year"),
        vehicle.get("make"),
        vehicle.get("model"),
        pk
    )
    statement = """
        UPDATE user
        SET year=?,
        make=?,
        model=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def deactivate(pk):
    cursor = get_db()
    cursor.execute("UPDATE user SET active=0 WHERE id=?", (pk,))
    cursor.commit()
    cursor.close()
