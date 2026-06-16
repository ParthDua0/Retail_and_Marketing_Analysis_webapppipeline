# ========================================================================
# SECTION 7: INTERACTIVE B2B SUPPLY CHAIN OPERATIONS DASHBOARD
# ========================================================================

import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

# 1. Supply Chain Ingestion Blueprint
required_artifacts = {
    'sales': 'data/processed/cleaned_retail_sales.csv',
    'rfm': 'data/processed/supplier_segments.csv',
    'kpis': 'data/processed/monthly_kpis.csv'
}

# Pre-flight data validation check
for key, path in required_artifacts.items():
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Missing required engine artifact: '{path}'. "
            "Please ensure upstream notebook cells have executed completely."
        )

df_sales = pd.read_csv(required_artifacts['sales'])
rfm = pd.read_csv(required_artifacts['rfm'])
monthly_kpis = pd.read_csv(required_artifacts['kpis'])

# Parse time vectors safely
df_sales['MONTH-PERIOD'] = pd.to_datetime(df_sales['MONTH-PERIOD'], errors='coerce')
monthly_kpis['Month_Period'] = pd.to_datetime(monthly_kpis['Month_Period'], errors='coerce')

# 2. Executive B2B Logistics KPI Calculations
val_col = 'TOTAL_SALES_VOLUME'  # Hardcoded baseline from verified columns list
total_volume = df_sales[val_col].sum()
active_suppliers = df_sales['SUPPLIER'].nunique()
mean_sku_volume = df_sales['ITEM_AVG_VOLUME'].mean()
avg_friction = monthly_kpis['Avg_Transfer_Friction'].mean()

# 3. Initialize Dash Web Application with clear styling rules
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Supply Chain & Vendor Ops Dashboard"

# 4. UI Layout Grid Configuration
app.layout = dbc.Container([
    # Dashboard Main Header Banner
    dbc.Row([
        dbc.Col(html.Div([
            html.H1("B2B Supply Chain Logistics & Vendor Performance Dashboard", 
                    className="text-light p-3 mb-0 bg-dark rounded-top text-center", 
                    style={"fontWeight": "700", "letterSpacing": "1px"}),
            html.P("Enterprise Inventory Flow Analysis • FVM Supplier Segmentation Engine", 
                   className="text-center text-muted bg-light p-2 mb-4 border-bottom rounded-bottom font-monospace")
        ]), width=12)
    ]),
    
    # Financial & Operational Scorecards Row
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("TOTAL SALES VOLUME MANAGED", className="text-muted text-uppercase small font-weight-bold"),
                html.H3(f"{total_volume:,.0f} units", className="text-primary font-weight-bold")
            ])
        ], color="light", outline=True), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("ACTIVE SUPPLIER ROSTER", className="text-muted text-uppercase small font-weight-bold"),
                html.H3(f"{active_suppliers:,} Vendors", className="text-success font-weight-bold")
            ])
        ], color="light", outline=True), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("MEAN SKU VOLUME PROFILE", className="text-muted text-uppercase small font-weight-bold"),
                html.H3(f"{mean_sku_volume:,.2f} units", className="text-info font-weight-bold")
            ])
        ], color="light", outline=True), width=3),
        
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("MEAN TRANSFER FRICTION INDEX", className="text-muted text-uppercase small font-weight-bold"),
                html.H3(f"{avg_friction:.2f}x Ratio", className="text-warning font-weight-bold")
            ])
        ], color="light", outline=True), width=3)
    ], className="mb-4 g-3"),
    
    # Core Visualization Layout Panels (FIXED: All layout IDs now strictly match callback outputs)
    dbc.Row([
        dbc.Col(dbc.Card([dbc.CardBody([dcc.Graph(id='volume-trend')])]), width=8),
        dbc.Col(dbc.Card([dbc.CardBody([dcc.Graph(id='supplier-clusters')])]), width=4)
    ], className="mb-4 g-3"),
    
    dbc.Row([
        dbc.Col(dbc.Card([dbc.CardBody([dcc.Graph(id='item-type-share')])]), width=6),
        dbc.Col(dbc.Card([dbc.CardBody([dcc.Graph(id='regional-sales')])]), width=6)
    ], className="g-3")
    
], fluid=True, style={"padding": "20px", "backgroundColor": "#f8f9fa"})

# ========================================================================
# PLOTLY INTERACTIVE CALLBACKS
# ========================================================================

@app.callback(
    Output('volume-trend', 'figure'),
    Input('volume-trend', 'id')
)
def update_volume_trajectory(_):
    fig = px.line(monthly_kpis, x='Month_Period', y='Total_Volume',
                  title='Macro Distribution Pipeline (Monthly Cargo Volume Velocity)',
                  markers=True, template='plotly_white')
    fig.update_traces(line=dict(width=3, color='#2c3e50'))
    fig.update_layout(title_font=dict(size=13, color="#2c3e50"))
    return fig

@app.callback(
    Output('supplier-clusters', 'figure'),
    Input('supplier-clusters', 'id')
)
def update_supplier_pies(_):
    counts = rfm['Cluster_Name'].value_counts()
    fig = px.pie(values=counts.values, names=counts.index,
                 title='FVM K-Means Cluster Allocations',
                 hole=0.45, color_discrete_sequence=px.colors.qualitative.Safe)
    fig.update_layout(title_font=dict(size=13))
    return fig

@app.callback(
    Output('item-type-share', 'figure'),
    Input('item-type-share', 'id')
)
def update_item_type_bars(_):
    shares = df_sales.groupby('ITEM TYPE')[val_col].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(shares, x='ITEM TYPE', y=val_col,
                 title='Inventory Allocation by Product Category Line',
                 color=val_col, color_continuous_scale='Blues', template='plotly_white')
    fig.update_layout(title_font=dict(size=13))
    return fig

@app.callback(
    Output('regional-sales', 'figure'),
    Input('regional-sales', 'id')
)
def update_regional_splits(_):
    # Fallback checking if columns match 'City' or another geographical label
    geo_col = 'City' if 'City' in df_sales.columns else df_sales.columns[1]
    geo = df_sales.groupby(geo_col)[val_col].sum().reset_index()
    fig = px.pie(geo, values=val_col, names=geo_col,
                 title='Geo-Logistical Regional Distribution Split',
                 hole=0.3, color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(title_font=dict(size=13))
    return fig

if __name__ == '__main__':
    # Streamlined modern execution command for unified server hosting
    app.run(debug=True, port=8050)