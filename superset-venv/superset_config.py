import logging

# Security Keys
ASYNC_QUERY_JWT_SECRET = "f95bd9732f0b42d0a0b11978a6d0c4621b7e6fabc0edb83a5135e314b36fc5d7"
SECRET_KEY = "tSALv4bDcdrYdieZI0UUQqlAR_phKNYJD3pkj2rePc0"

APP_NAME = "Healthray"
APP_ICON = "/static/assets/images/logo.jpg"
APP_ICON_WIDTH = 1000
LOGO_TARGET_PATH = "/"
LOGO_TOOLTIP = "Go Home"
FAVICONS = [{"href": "/static/assets/images/logo.png"}]



THEME_OVERRIDES = {
    
    "colors": {

        "text": {
            "label": '#879399',
            "help": '#737373'
        },

        # "primary": {
        #     "base": 'red',
        # },
        "secondary": {
            "base": 'green',
        },
        # "grayscale": {
        #     "base": 'orange',
        # },
        "error":{
            "base": 'Pink'
        }
    },


    "typography": {
        "families": {
        "sansSerif": 'Inter',
        "serif": 'Georgia',
        "monospace": 'Fira Code',
        },
        "weights": {
            "light": 200,
            "normal": 400,
            "medium": 500,
            "bold": 600
        }
	}
}


EXTRA_CATEGORICAL_COLOR_SCHEMES = [
     {
         "id": 'world_population_reporting_colors',
         "description": '',
         "label": 'World Population Reporting colors',
         "colors": ['#004369', '#65D0E4', '#50BEF3', '#65D0E4', '#7D82EA', '#AA5ECB', '#CE42A1', '#EC487D', '#FA6E67', '#FFA064', '#EEDD55', '#9977BB', '#BBAA44', '#DDCCDD']
     },
     {
         "id": 'neon_pastel_colors',
         "description": '',
         "label": 'Neon Pastel colors (Trendy + Modern)',
         "colors": ["#F72585", "#B5179E", "#7209B7", "#560BAD", "#480CA8", "#3A0CA3", "#3F37C9", "#4361EE", "#4895EF", "#4CC9F0"]

     },
     {
         "id": 'material_design_palette_colors',
         "description": '',
         "label": ' Material Design Palette',
         "colors": ["#2196F3", "#03A9F4", "#00BCD4", "#009688", "#4CAF50", "#8BC34A", "#CDDC39", "#FFC107", "#FF9800", "#FF5722"]

     },
     {
         "id": 'soft_candy_colors',
         "description": '',
         "label": 'Soft Candy Colors (Calm & UI Friendly)',
         "colors": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#D3C0F9", "#F9C0C0", "#C0F9E8", "#E0C0F9", "#F9E6C0"]
     },
     {
         "id": 'dark_mode_palette',
         "description": '',
         "label": 'Dark Mode Palette (High Contrast)',
         "colors": ["#FF6B6B", "#F06595", "#CC5DE8", "#845EF7", "#5C7CFA", "#339AF0", "#22B8CF", "#20C997", "#51CF66", "#94D82D"]


     },
     {
         "id": 'viridis_colors',
         "description": '',
         "label": 'Viridis (Scientific / Heatmap Friendly)',
         "colors": ["#440154", "#482777", "#3F4A8A", "#31688E", "#26828E", "#1F9E89", "#35B779", "#6DCD59", "#B4DD2C", "#FDE725"]
     }]



# Optional: Logging to verify config is loaded
print("✅ Superset config loaded.")