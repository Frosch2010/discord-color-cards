class cc_variables:

    cc_carddeck_template = ["r:1","r:1","r:2","r:2","r:3","r:3","r:4","r:4","r:5","r:5","r:6","r:6","r:7","r:7","r:8","r:8","r:9","r:9", "r:๐", "r:๐", "r:๐", "r:๐ซ", "r:๐ซ", "r:โ", "r:โซ", "r:โซ",
                      "g:1","g:1","g:2","g:2","g:3","g:3","g:4","g:4","g:5","g:5","g:6","g:6","g:7","g:7","g:8","g:8","g:9","g:9", "g:๐", "g:๐", "g:๐", "g:๐ซ", "g:๐ซ", "g:โ", "g:โซ", "g:โซ",
                      "b:1","b:1","b:2","b:2","b:3","b:3","b:4","b:4","b:5","b:5","b:6","b:6","b:7","b:7","b:8","b:8","b:9","b:9", "b:๐", "b:๐", "b:๐", "b:๐ซ", "b:๐ซ", "b:โ", "b:โซ", "b:โซ",
                      "y:1","y:1","y:2","y:2","y:3","y:3","y:4","y:4","y:5","y:5","y:6","y:6","y:7","y:7","y:8","y:8","y:9","y:9", "y:๐", "y:๐", "y:๐", "y:๐ซ", "y:๐ซ", "y:โ", "y:โซ", "y:โซ",
                      "wi:๐ณ", "wi:๐ณ", "wi:๐ณ", "wi:๐ณ", "wi:โ", "wi:โ", "wi:๐จโ๐จโ๐งโ๐ฆ", "wi:๐จโ๐จโ๐งโ๐ฆ"]

    cc_current_carddeck = ["r:1","r:1","r:2","r:2","r:3","r:3","r:4","r:4","r:5","r:5","r:6","r:6","r:7","r:7","r:8","r:8","r:9","r:9", "r:๐", "r:๐", "r:๐", "r:๐ซ", "r:๐ซ", "r:โ", "r:โซ", "r:โซ",
                      "g:1","g:1","g:2","g:2","g:3","g:3","g:4","g:4","g:5","g:5","g:6","g:6","g:7","g:7","g:8","g:8","g:9","g:9", "g:๐", "g:๐", "g:๐", "g:๐ซ", "g:๐ซ", "g:โ", "g:โซ", "g:โซ",
                      "b:1","b:1","b:2","b:2","b:3","b:3","b:4","b:4","b:5","b:5","b:6","b:6","b:7","b:7","b:8","b:8","b:9","b:9", "b:๐", "b:๐", "b:๐", "b:๐ซ", "b:๐ซ", "b:โ", "b:โซ", "b:โซ",
                      "y:1","y:1","y:2","y:2","y:3","y:3","y:4","y:4","y:5","y:5","y:6","y:6","y:7","y:7","y:8","y:8","y:9","y:9", "y:๐", "y:๐", "y:๐", "y:๐ซ", "y:๐ซ", "y:โ", "y:โซ", "y:โซ",
                      "wi:๐ณ", "wi:๐ณ", "wi:๐ณ", "wi:๐ณ", "wi:โ", "wi:โ", "wi:๐จโ๐จโ๐งโ๐ฆ", "wi:๐จโ๐จโ๐งโ๐ฆ"]

    cc_red_card_template = "๐ฅ๐ฅ๐ฅ|๐ฅ  **NUM**  ๐ฅ    COUNT|๐ฅ๐ฅ๐ฅ"
    cc_blue_card_template = "๐ฆ๐ฆ๐ฆ|๐ฆ  **NUM**  ๐ฆ    COUNT|๐ฆ๐ฆ๐ฆ"
    cc_green_card_template = "๐ฉ๐ฉ๐ฉ|๐ฉ  **NUM**  ๐ฉ    COUNT|๐ฉ๐ฉ๐ฉ"
    cc_yellow_card_template = "๐จ๐จ๐จ|๐จ  **NUM**  ๐จ    COUNT|๐จ๐จ๐จ"
    cc_wish_card_template = "๐ณ๐ฅ๐ณ|๐ฆ  **NUM**  ๐ฉ    COUNT|๐ณ๐จ๐ณ"


    cc_current_mid_card = ""

    cc_current_wish_color = ""

    cc_player_list = []
    cc_player_display_list = ""
    cc_player_hand = []
    cc_player_str_hand = []
    

    cc_current_player = 0


    cc_is_running = False
    cc_is_reversed = False


    cc_is_lay_card_reacting = False
    cc_next_react_is_number = False
    cc_player_lay_card_reacting = None
    cc_lay_card_react_message = None
    cc_lay_card_possible_colors = []
    cc_lay_card_possible_numbers = []
    cc_lay_card_react_choosed_color = ""


    cc_is_wish_reacting = False
    cc_player_wish_reacting = None
    cc_wish_react_message = None
    cc_wish_react_card_num = None


    cc_card_messages = []
    cc_player_card_str = []


    cc_rotate_player_hands = False

    cc_player_is_suspend = False
    cc_suspended_player_can_lay = False


    cc_plus_card_amount = 0
    cc_plus_player_can_lay = False
    cc_plus_print = False


    cc_wish_next_player_get_cards = False