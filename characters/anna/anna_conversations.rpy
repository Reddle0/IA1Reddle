label anna_convo_default:
    call process_conversation_beginning([ (n, ""), (anna, "") ])
    anna.c "H-hi, [n.say_name]..."

    call process_end_of_conversation("anna_convo_default", anna, priority = False, default = True)

    return