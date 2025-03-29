class MultiDBRouter:
    def db_for_read(self, model, **hints):
        """Point database operations for specific models to the right database."""
        if model._meta.app_label == 'customer':
            return 'mysql'  # MySQL
        elif model._meta.app_label in ['cart', 'order', 'shipping', 'paying']:
            return 'postgres'  # PostgreSQL
        elif model._meta.app_label in ['book', 'mobile', 'clothes', 'shoes', 'comment']:
            return 'mongo'  # MongoDB
        return None

    def db_for_write(self, model, **hints):
        """Same logic as db_for_read for write operations."""
        return self.db_for_read(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure only the intended models get migrated to each database."""
        if app_label == 'customer':
            return db == 'mysql'
        elif app_label in ['cart', 'order', 'shipping', 'paying']:
            return db == 'postgres'
        elif app_label in ['book', 'mobile', 'clothes', 'shoes', 'comment']:
            return False
        return None
