import pandas as pd
from .models import District, db

def load_data():
    df = pd.read_csv('socioeconomic_and_climate_data_for_german_districs.csv')
    
    # Calculate percentiles for vulnerability indices
    df['socioeconomic_percentile'] = df['socioeconomic_vulnerability_index'].rank(pct=True) * 100
    df['climate_percentile'] = df['climate_vulnerability_index'].rank(pct=True) * 100
    
    for _, row in df.iterrows():
        print(row['tropennächte_jetzt'], type(row['tropennächte_jetzt']))
        district = District(
            kommune=row['Kommune'],
            bundesland=row['Bundesland'],
            low_income=row['Haushalte mit niedrigem Einkommen (%)'],
            general_funds=row['Allgemeine Deckungsmittel (Euro je Einwohner:in)'],
            elderly_percentage=row['Anteil ab 65-Jährige (%)'],
            long_term_unemployment=row['Langzeitarbeitslosenquote (%)'],
            debt=row['Verschuldung im Kernhaushalt (Euro je Einwohner:in)'],
            admin_type=row['Verwaltungstyp'],
            socioeconomic_vulnerability=row['socioeconomic_vulnerability_index'],
            heavy_rain_current=row['starkregentage_jetzt'],
            heavy_rain_future=row['starkregentage_zukunft'],
            dry_days_current=row['trockentage_jetzt'],
            dry_days_future=row['trockentage_zukunft'],
            hot_days_current=row['heiße_tage_jetzt'],
            hot_days_future=row['heiße_tage_zukunft'],
            humid_days_current=row['schwüle_tage_jetzt'],
            humid_days_future=row['schwüle_tage_zukunft'],
            tropical_nights_current=row['tropennächte_jetzt'],
            tropical_nights_future=row['tropennächte_zukunft'],
            climate_vulnerability=row['climate_vulnerability_index']
        )
        db.session.add(district)
    
    db.session.commit()

def get_policy_recommendations(district):
    recommendations = {
        'socioeconomic': [],
        'climate': []
    }
    
    # Socioeconomic recommendations
    if district.low_income > 20:
        recommendations['socioeconomic'].append(
            "Consider implementing local economic development programs and job training initiatives"
        )
    if district.long_term_unemployment > 5:
        recommendations['socioeconomic'].append(
            "Focus on creating partnerships with local businesses for job placement programs"
        )
    if district.elderly_percentage > 25:
        recommendations['socioeconomic'].append(
            "Develop programs specifically targeted at senior citizens' needs"
        )
    
    # Climate recommendations
    if district.hot_days_future > 5:
        recommendations['climate'].append(
            "Implement urban greening initiatives and increase shade coverage"
        )
    if district.heavy_rain_future > 3:
        recommendations['climate'].append(
            "Enhance flood protection measures and improve drainage systems"
        )
    if district.dry_days_future > 10:
        recommendations['climate'].append(
            "Develop drought management strategies and water conservation programs"
        )
    
    return recommendations