import pygame
from abc import ABC, abstractmethod

class MovementStrategy(ABC):
    @abstractmethod
    def update_position(self, animation):
        pass

class NoMovementStrategy(MovementStrategy):
    def __init__(self):
        pass
    def update_position(self, animation):
        animation.x = animation.x
        animation.y = animation.y

class LinearStraightMovementStrategy(MovementStrategy):
    def __init__(self, initial_pos, final_pos, moving_time):
        self.updates_done = 0
        self.x_per_update, self.y_per_update, self.total_updates = self.calculate_updates(initial_pos, final_pos, moving_time)

    def calculate_updates(self, initial_pos, final_pos, moving_time):
        initial_x, initial_y = initial_pos
        final_x, final_y = final_pos
        total_updates = round(moving_time * 60)
        x_per_update = (final_x - initial_x) / total_updates
        y_per_update = (final_y - initial_y) / total_updates

        return x_per_update, y_per_update, total_updates

    def update_position(self, animation):
        if self.updates_done < self.total_updates:
            animation.x += self.x_per_update
            animation.y += self.y_per_update
            animation.x %= animation.screen.get_width()
            animation.y %= animation.screen.get_height()
            self.updates_done += 1



class Animation:
    def __init__(self, screen, delay_per_frame, sprite_sheet, initial_pos, final_pos, moving_time, moving_strategy=None, scale=1):
        self.screen = screen
        self.current_frame = 0
        self.delay_counter = 0
        self.delay_per_frame = delay_per_frame
        self.sprite_sheet = sprite_sheet
        self.animation_frames = self.sprite_sheet.get_images()
        self.x, self.y = initial_pos
        self.movement_strategy = moving_strategy if moving_strategy else LinearStraightMovementStrategy(initial_pos, final_pos, moving_time)

    def update_frame(self):
        if self.delay_counter % self.delay_per_frame == 0:
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
        self.delay_counter += 1

    def update_position(self):
        self.movement_strategy.update_position(self)

    def update(self):
        self.update_frame()
        self.update_position()

    def draw(self):
        x = round(self.x)
        y = round(self.y)
        rect = self.animation_frames[self.current_frame].get_rect(center=(x, y))
        self.screen.blit(self.animation_frames[self.current_frame], rect)