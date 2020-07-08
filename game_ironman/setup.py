import cx_Freeze

executables=[cx_Freeze.Executable("menu.py")]

cx_Freeze.setup(
    name="IronMan Racer",
    options={"build_exe":{"packages":["pygame"],
    "include_files": [
        "falcon.jpg",
"falcon_dp.jpg",
"falcon_dp2.png",
"falcon2.png",
"fireball.png",
"game.py",
"ironbg.jpg",
"ironman_dp.png",
"ironmanflysmall.png",
"ironmanflysmall150.png",
"menu_bg.jpg",
"quinjet.jpg",
"quinjet2.png",
"rockbg.png",
"D:/Desktop/try/game_ironman/thor.jpg",
"D:/Desktop/try/game_ironman/thor_dp.jpg",
"D:/Desktop/try/game_ironman/thor_dp2.png",
"D:/Desktop/try/game_ironman/thor1.png",
"vision.jpg",
"vision_dp.png",
"vision_fly.png",
"vision_fly_small.png",
"war_dp.jpg",
"war_dp2.png",
"war_machine.jpg",
"war_machine2.png","bg_player.jpg","player_choose.py"



        ]}},
    executables= executables
    )



