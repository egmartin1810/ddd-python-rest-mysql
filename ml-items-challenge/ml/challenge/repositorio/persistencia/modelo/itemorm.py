from main import db


class ItemORM(db.Model):
    # Nombre de la tabla en BD
    __tablename__ = "item"
    # Atributos de la tabla ITEM
    site = db.Column(db.String(4), primary_key=True)
    id = db.Column(db.String(12), primary_key=True)
    price = db.Column(db.Float, nullable=True)
    start_time = db.Column(db.String(30), nullable=True)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(80), nullable=True)
    nickname = db.Column(db.String(40), nullable=True)

    def save(self):
        print("El estado del pool de la BD es: " + db.engine.pool.status())
        db.session.add(self)
        db.session.commit()

    def deleteAll(self):
        print("Eliminando TODOS los datos persistidos de Items...")
        registrosEliminados = db.session.query(ItemORM).delete()
        db.session.commit()
        print("Saliendo de ItemORM.deleteAll, Registros Eliminados: ", registrosEliminados)
        return registrosEliminados

    def __repr__(self):
        return '<Item {}>'.format(self.site+str(self.id))
