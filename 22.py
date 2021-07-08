CACHE={}

def battle(hp, bosshp, boss_damage, mana, shield_turns=0, poison_turns=0, recharge_turns=0, mana_spent=0, player_turn=True):
    armor = 7 if shield_turns else 0
    poison = 3 if poison_turns else 0
    recharge = 101 if recharge_turns else 0

    assert poison_turns <= 6
    assert recharge_turns <= 5
    assert shield_turns <= 6
    shield_turns = shield_turns - 1 if shield_turns else 0
    poison_turns = poison_turns - 1 if poison_turns else 0
    recharge_turns = recharge_turns - 1 if recharge_turns else 0

    bosshp -= poison
    mana += recharge

    if bosshp <= 0:
        return True, mana_spent

    if mana == 0:
        return False, mana_spent

    assert mana > 0

    if not player_turn:
        incoming_damage = max(0, boss_damage - armor)
        # Damage player, if lost, this is a dead path.
        hp -= incoming_damage
        if hp <= 0:
            return False, mana_spent
        else:
            return battle(hp, bosshp, boss_damage, mana, shield_turns, poison_turns, recharge_turns, mana_spent, True)

    # Part 2 hard mode.
    hp -= 1
    if hp <= 0:
        return False, mana_spent

    results = []
    # Otherwise, try one of each action, assuming that it isn't already active
    if not shield_turns:
        if mana >= 113:
            results.append(battle(hp, bosshp, boss_damage, mana - 113, 6, poison_turns, recharge_turns, mana_spent + 113, False))
    if not poison_turns:
        if mana >= 173:
            results.append(battle(hp, bosshp, boss_damage, mana - 173, shield_turns, 6, recharge_turns, mana_spent + 173, False))
    if not recharge_turns:
        if mana >= 229:
            results.append(battle(hp, bosshp, boss_damage, mana - 229, shield_turns, poison_turns, 5, mana_spent + 229, False))

    # Drain
    if mana >= 73:
        results.append(battle(hp + 2, bosshp - 2, boss_damage, mana - 73, shield_turns, poison_turns, recharge_turns, mana_spent + 73, False))

    # magic missile
    if mana >= 53:
        results.append(battle(hp, bosshp - 4, boss_damage, mana - 53, shield_turns, poison_turns, recharge_turns, mana_spent + 53, False))

    # print(results)
    # return the best
    best = 10000000000000
    for (won, spent) in results:
        if won and spent < best:
            best = spent

    if best < 10000000000000:
        # print("Won, ", mana_spent, mana)
        return True, best
    else:
        return False, best


# print(battle(10, 13, 8, 250))

# print(battle(10, 14, 8, 250))

print(battle(50, 71, 10, 500)) # 1010 too low. 1824
