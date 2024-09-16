from flask import render_template_string,render_template
from flask_security import auth_required,current_user,roles_required,roles_accepted

def create_view(app):
    @app.route('/')
    def index():
        return render_template('index.html')
        
    @app.route('/profile')
    @auth_required('session','token')
    def profile():
        return render_template_string(
            """
                <h1> This is the profile page </h1>
                <h1> WELCOME !{{ current_user.email }} </h1>
                <a href="/logout">logout</a>
                
            """
            
        )
    
    @app.route('/inst_dashboard')
    @roles_required('inst')
    def inst_dashboard():
        return render_template_string(
            """
            <h1>Instructor Dashboard </h1>
            """
            
        )
