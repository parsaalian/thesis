class PrimaryRouter:
    def db_for_read(self, model, **hints):
        return 'default'


    def db_for_write(self, model, **hints):
        return 'default'


    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == 'default' and obj2._state.db == 'default':
            return True
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True