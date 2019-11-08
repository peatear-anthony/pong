import pygame
import sys

def update_screen(settings, screen, paddles, ball):
    screen.fill(settings.bg_color)
    for paddle in paddles:
        paddle.draw_paddle()
    ball.draw_ball()
    pygame.display.flip()

def check_events(settings, screen, paddles, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            __check_keydown_events(event, settings, paddles)
        elif event.type == pygame.KEYUP:
            __check_keyup_events(event, settings, paddles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            return

def update_ball(settings, screen, paddles, ball):
    ball.update()
    check_ball_collisions(settings, screen, paddles, ball)

def check_ball_collisions(settings, screen, paddles, ball):
    if ball.rect.top <= paddles[0].rect.bottom:
        check_ball_paddle_collisions(settings, screen, paddles, ball)
    elif ball.rect.bottom >= paddles[1].rect.top:
        check_ball_paddle_collisions(settings, screen, paddles, ball)
    elif ball.rect.left <= 0:
        hit_left_wall()
    elif ball.rect.right >= screen.get_rect().right:
        hit_right_wall()

def check_ball_paddle_collisions(settings, screen, paddles, ball):
    if pygame.sprite.collide_rect(ball, paddles[0]):
        __calc_dist_from_center(ball.rect.centerx, 
            paddles[0].rect.centerx)

    elif pygame.sprite.collide_rect(ball, paddles[1]):
        __calc_dist_from_center(ball.rect.centerx, 
            paddles[1].rect.centerx)

def hit_left_wall():
    print("To do")

def hit_right_wall():
    print("To do")



##########################Privite functions####################################

def __check_keydown_events(event, settings, paddles):
    if event.key == pygame.K_RIGHT:
        paddles[0].moving_right = True
    elif event.key == pygame.K_LEFT:
        paddles[0].moving_left = True
    elif event.key == pygame.K_d:
        paddles[1].moving_right = True
    elif event.key == pygame.K_a:
        paddles[1].moving_left = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def __check_keyup_events(event, settings, paddles):
    if event.key == pygame.K_RIGHT:
        paddles[0].moving_right = False
    elif event.key == pygame.K_LEFT:
        paddles[0].moving_left = False
    elif event.key == pygame.K_d:
        paddles[1].moving_right = False
    elif event.key == pygame.K_a:
        paddles[1].moving_left = False

def __calc_dist_from_center(ball_x, paddle_x):
    print("lol")