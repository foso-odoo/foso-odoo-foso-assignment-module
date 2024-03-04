{
    'name': "Transport Management System",
    'version': '1.0',
    'depends': ['base','stock_picking_batch','fleet'],
    'author': "Foram Solanki",
    'description': """This is the Real Estate Module which describes what is expected price for property for seller and buyer can see this
    """,
    'application': True,
  
    'data': [
        
        'views/fleet_vehicle_category_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_batch_pick_views.xml',
        
        ],
    
    
}