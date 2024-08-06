import psycopg2
from ConnectDataBaseHot import ConnectToDatabaseHOT

class QuerysViewsDashboard(ConnectToDatabaseHOT):
    def __init__(self):
        super().__init__()
        
        self.cursor_views = self.ConnectDatabaseHOT.cursor()
        
        self.QueryView_DashboardCancelamentos = "SELECT * FROM dashboardcancelamentos"
        self.QueryView_DashboardClientes = "SELECT * FROM dashboardclientes"
        self.QueryView_DashboardRevendasDesempenho = "SELECT * FROM dashboardrevendasdesempenho"
        self.QueryView_DashboardRevendas = "SELECT * FROM dashboardrevenda"
        
        
        try:
            self.cursor_views.execute(self.QueryView_DashboardCancelamentos)
            self.cursor_views.fetchall()
            
            self.cursor_views.execute(self.QueryView_DashboardClientes)
            self.cursor_views.fetchall()
            
            self.cursor_views.execute(self.QueryView_DashboardRevendasDesempenho)
            self.cursor_views.fetchall()
            
            self.cursor_views.execute(self.QueryView_DashboardRevendas)
            self.cursor_views.fetchall()
            
        except Exception as e:
            print('Erro in query: ', {e})
            
            