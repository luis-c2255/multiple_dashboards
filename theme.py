class Colors:
    DARKTEAL = "#005F73"
    DARKCYAN = "#0A9396"
    
class Components:
    @staticmethod
    def page_header(title:str) -> str:
        """Create a styled page header"""
        return f"""
        <div style='background: linear-gradient(135deg, {Colors.DARKTEAL} 0%, {Colors.DARKCYAN} 100%);
                    padding: 0.8rem; border-radius: 8px; margin-bottom: 0.8rem;'>
                    <h1 style='color: white; margin: 0; text-align: center; font-size: 2.5rem;'>{title}</h1>
        </div>
        """