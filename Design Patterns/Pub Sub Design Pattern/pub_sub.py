from pubsub import pub


def listener_1(arg):
    print('Listener1 receives news about', arg['headline'])
    print(arg['news'])
    print()


def listener_2(arg):
    print('Listener2 receives news about', arg['headline'])
    print(arg['news'])
    print()


pub.subscribe(listener_1, 'football')
pub.subscribe(listener_2, 'chess')


pub.sendMessage('football', arg={'headline': 'Ronaldo',
                                 'news': 'Sold for $1M'})
pub.sendMessage('chess', arg={'headline': 'AI',
                              'news': 'Terminator is back!!'})
pub.sendMessage('football', arg={'headline': 'Messi',
                                 'news': 'Sold for $3M'})