/*
2 players, the entire deck is divided equally between them
They reveal the top card each, and the player with the higher card places both cards face down to themselves
The player without cards loses

Let all cards be different
and the smaller one beats the larger one

The player who takes the cards first places the first player's card first

In the game, there are 10 cards from 0 to 9. 0 beats 9

Solution - 2 queues until one of them is empty
*/

#include "../../utils/Queue.h"

#include <iostream>


const int INIT_CARDS = 5;

void cardDistribution(std::istream&in, Queue<int>& player) {
    for (int i = 0; i < INIT_CARDS; i++) {
        int card;
        in >> card;
        player.push(card);
    }
}

bool isWinableCard(int winableCard, int losableCard) {
    return winableCard != 9 && winableCard > losableCard 
        || winableCard == 9 && losableCard != 0 
        || winableCard == 0 && losableCard == 9;
}

int simulateDrunkedGame(Queue<int>& fPlayer, Queue<int>& sPlayer) {
    int moves = 0;
    while (fPlayer.size() > 0 && sPlayer.size() > 0) {
        int fPlayerCard = fPlayer.pop();
        int sPlayerCard = sPlayer.pop();
        if (isWinableCard(fPlayerCard, sPlayerCard)) {
            fPlayer.push(fPlayerCard);
            fPlayer.push(sPlayerCard);
        } else {
            sPlayer.push(fPlayerCard);
            sPlayer.push(sPlayerCard);
        }
        moves++;
    }

    return moves;
}

int main()
{
    Queue<int> firstPlayer(10);
    Queue<int> secondPlayer(10);
    cardDistribution(std::cin, firstPlayer);
    cardDistribution(std::cin, secondPlayer);

    int moves = simulateDrunkedGame(firstPlayer, secondPlayer);

    std::cout << (firstPlayer.size() == 0 ? "second" : "first") << " " << moves;
    return 0;
}
