class GameStats():
    """游戏状态类"""
    
    def __init__(self, ai_settings):
        """初始化游戏设置"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 启动后默认状态为没有开始
        self.game_active = False
        
        # 最高分
        self.high_score = 0
        
    def reset_stats(self):
        """恢复默认设置"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
