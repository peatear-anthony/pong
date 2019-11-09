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
        hit_wall_update_speed(ball)
    elif ball.rect.right >= screen.get_rect().right:
        hit_wall_update_speed(ball)

def check_ball_paddle_collisions(settings, screen, paddles, ball):
    if pygame.sprite.collide_rect(ball, paddles[0]):
        __update_ball_speed(settings,ball, paddles[0])

    elif pygame.sprite.collide_rect(ball, paddles[1]):
        __update_ball_speed(settings, ball, paddles[1])

def hit_wall_update_speed(ball):
    ball.vel_x *= -1


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

def __update_ball_speed(settings, ball, paddle):
    norm_ball_x = int(ball.rect.centerx - paddle.rect.left)

    if norm_ball_x <=0:
        norm_ball_x = 1
    elif norm_ball_x >= paddle.rect.width:
        norm_ball_x = paddle.rect.width

    ball.vel_x = settings.ball_speed_magnitude *\
        settings.paddlex_to_velx[norm_ball_x]

    if paddle.player == 1:
        ball.vel_y = settings.ball_speed_magnitude *\
        settings.paddlex_to_vely[norm_ball_x]
    elif paddle.player ==2:
        ball.vel_y = -1* settings.ball_speed_magnitude *\
        settings.paddlex_to_vely[norm_ball_x]