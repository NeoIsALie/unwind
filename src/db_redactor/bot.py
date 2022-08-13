import time

import telebot
from typing import List
from datetime import datetime


class OrderBot:
    def __init__(self,
                 bot_token: str,
                 user_id: str
                 ):
        self.bot = telebot.TeleBot(bot_token)
        self.user_id = user_id

    def check_order(self, orders: List[List]):
        """
        Check if order date is out of deadline
        :param orders: list of orders
        """
        for order in orders:
            if datetime.strptime(order[3], '%d.%m.%Y').date() < datetime.now().date():
                message = f'Cрок поставки заказа №{order[2]} вышел {order[3]}!'
                self.bot.send_message(self.user_id, message)
                time.sleep(2)
