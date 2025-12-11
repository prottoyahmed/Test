from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    from app.routes.main import main_bp
    from app.routes.blog import blog_bp
    from app.routes.portfolio import portfolio_bp
    from app.routes.contact import contact_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    
    return app