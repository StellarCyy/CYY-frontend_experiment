import datetime
import easygui
class VisitorNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # 基本信息
        ip = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')

        # 解析 User-Agent 获取设备信息
        device_info = self.parse_user_agent(user_agent)

        print(f"📱 设备: {device_info}")
        print(f"🌐 浏览器: {user_agent}")
        return self.get_response(request)

    def parse_user_agent(self, user_agent):
        """简单解析 User-Agent"""
        ua = user_agent.lower()
        if 'mobile' in ua:
            return '手机'
        elif 'tablet' in ua:
            return '平板'
        elif 'windows' in ua:
            return 'Windows电脑'
        elif 'mac' in ua:
            return 'Mac电脑'
        elif 'linux' in ua:
            return 'Linux电脑'
        else:
            return '未知设备'

    def get_client_ip(self, request):
        """获取访客真实 IP"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip