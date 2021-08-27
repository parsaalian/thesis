pragma solidity ^0.8.7;

contract Bet {
    uint constant STATUS_WIN = 1;
    uint constant STATUS_LOSE = 2;
    uint constant STATUS_TIE = 3;
    uint constant STATUS_PENDING = 4;

    uint constant STATUS_NOT_STARTED = 1;
    uint constant STATUS_STARTED = 2;
    uint constant STATUS_COMPLETE = 3;
    uint constant STATUS_ERROR = 4;

    struct Better {
        uint guess;
        address addr;
        uint status;
    }

    struct Game {
        uint256 betAmount;
        uint outcome;
        uint status;
        Better[16] originators;
        Better[16] takers;
    }

    Game game;
}

    function createBet(uint _guess) public payable {
        game = Game(msg.value, 0, STATUS_STARTED, Better(_guess, msg.sender, STATUS_PENDING), Better(0, 0, STATUS_NOT_STARTED));
        game.originator = Better(_guess, msg.sender, STATUS_PENDING);
    }

    function takeBet(uint _guess) public payable { 
      //requires the taker to make the same bet amount     
      require(msg.value == game.betAmount);
      game.taker = Better(_guess, msg.sender, STATUS_PENDING);
      generateBetOutcome();
    }

    function generateBetOutcome() private {
        //todo - not a great way to generate a random number but ok for now
        game.outcome = uint(block.blockhash(block.number-1)) % 10 + 1;
        game.status = STATUS_COMPLETE;

        if (game.originator.guess == game.taker.guess) {
          game.originator.status = STATUS_TIE;
          game.taker.status = STATUS_TIE;
        } else if (game.originator.guess > game.outcome && game.taker.guess > game.outcome) {
          game.originator.status = STATUS_TIE;
          game.taker.status = STATUS_TIE;
        } else {
           if ((game.outcome - game.originator.guess) < (game.outcome - game.taker.guess)) {
             game.originator.status = STATUS_WIN;
             game.taker.status = STATUS_LOSE;
           } else if ((game.outcome - game.taker.guess) < (game.outcome - game.originator.guess)) {
             game.originator.status = STATUS_LOSE;
             game.taker.status = STATUS_WIN;
           } else {
             game.originator.status = STATUS_ERROR;
             game.taker.status = STATUS_ERROR;
             game.status = STATUS_ERROR;
           }
        }
    }
}