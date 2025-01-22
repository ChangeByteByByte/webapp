from flask import Blueprint, render_template, jsonify, request
from .models import District
from .utils import get_policy_recommendations
from sqlalchemy import func

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search')
def search():
    query = request.args.get('q', '')
    districts = District.query.filter(
        func.lower(District.kommune).contains(query.lower())
    ).limit(1)
    return jsonify([d.kommune for d in districts])

@main.route('/district/<kommune>')
def district_details(kommune):
    district = District.query.filter_by(kommune=kommune).first_or_404()
    
    # Calculate percentiles
    socio_percentile = District.query.filter(
        District.socioeconomic_vulnerability < district.socioeconomic_vulnerability
    ).count() / District.query.count() * 100
    
    climate_percentile = District.query.filter(
        District.climate_vulnerability < district.climate_vulnerability
    ).count() / District.query.count() * 100
    
    recommendations = get_policy_recommendations(district)
    
    return render_template('district.html', 
                         district=district,
                         socio_percentile=socio_percentile,
                         climate_percentile=climate_percentile,
                         recommendations=recommendations)