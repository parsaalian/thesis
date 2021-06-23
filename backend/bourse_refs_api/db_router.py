class BourseRefsApiDBRouter:
    """
    A router to control all database operations on models in the
    bourse_refs_api application.
    """
    route_app_labels = {'bourse_refs_api'}


    def db_for_read(self, model, **hints):
        """
        Attempts to read bourse_refs_api models go to bourse_refs_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'bourse_refs_db'
        return None


    def db_for_write(self, model, **hints):
        """
        Prevent writes to bourse_refs_api models.
        """
        return None


    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the bourse_refs_api app is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Prevent migrations for bourse_refs_api models.
        """
        return None