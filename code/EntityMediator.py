from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, EnemyShot)):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.right > WIN_WIDTH:
                ent.health = 0


    @staticmethod
    def __shotEnemy_collision(players, ent: Entity):
        if isinstance(ent, EnemyShot):
            if players.instance:
                if ent.rect in players.rect:
                    ent.health -= 1
                    players.health -= 1



    @staticmethod
    def verify_collision(players, entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)
            EntityMediator.__shotPlayer_collision(entity_list, test_entity)
            for l in range(len(players)):
                players_test = players[l]
                EntityMediator.__shotEnemy_collision(players_test, test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def __shotPlayer_collision(entity_list, ent:Entity):
        if isinstance(ent, PlayerShot):
            for i in range(len(entity_list)):
                if isinstance (entity_list[i],Enemy):
                    if ent.rect in entity_list[i].rect:
                        ent.health -= 1
                        entity_list[i].health -= 1

