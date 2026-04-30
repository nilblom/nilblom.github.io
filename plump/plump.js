var PlumpGame = null;

function GUI_Score_SetScore(player, s, n) {
    var e = document.querySelector("#" + player + "-score-sticks");
    e.innerHTML = s;
    var e = document.querySelector("#" + player + "-score-taken-sticks");
    e.innerHTML = n;
}

function GUI_Scoreboard_Clear() {
    var e = document.querySelector("#player-scoreboard-scores");
    e.innerHTML = "";
    var e = document.querySelector("#cpu-scoreboard-scores");
    e.innerHTML = "";
}

function GUI_Scoreboard_AddScore(player, n) {
    var s = document.createElement("span");
    s.style.marginRight = "5px";
    s.innerText = n;
    var e = document.querySelector("#" + player + "-scoreboard");
    e.appendChild(s);
}

function GUI_CreateMenu() {
    var startGame = document.querySelector("#menu-start-game");
    startGame.onclick = function() {
        Plump_PlayGame();
        GUI_HideMenu();
    };
}

function GUI_DealCards(player, cards, hidden) {
    var e = document.querySelector("#" + player + "-area");
    for (const c of cards) {
        e.appendChild(GUI_Card_RenderCard(c, player, hidden));
    }
}

function GUI_PlayPlayerCardByClick(e) {
    var playArea = document.querySelector("#play-area");
    playArea.appendChild(e);
    var e = document.querySelector("#player-area");
    e.onclick = null;
}

function GUI_PlayCard(player, card, callback) {
    var e = document.querySelector("#" + player + "-area");
    var playArea = document.querySelector("#play-area");
    for (var i = 0; i < e.children.length; i++) {
        var c = e.children[i];
        if (c.id == "card" + card.suite + "_" + card.number) {
            playArea.appendChild(c);
            c.src = c.getAttribute("image-url");
            setTimeout(callback, 1000);
        }
    }
}

function GUI_ShowMenu() {
    var e = document.querySelector("#menu");
    e.style.display = "";
}

function GUI_HideMenu() {
    var e = document.querySelector("#menu-background");
    e.style.display = "none";
}

var Player = {
    number: null,
    cards: [],
    plump: false
};


var CPUPlayer = Player;

function Player_createPlayer() {
    return {...Player};
}

var Card = {
    suite: null,
    number: null
};

function GUI_Card_RenderCard(card, player, hidden) {
    var e = document.createElement("img");
    if (hidden == true) {
        e.src = "./images/back-red.png";
        e.setAttribute("image-url", "./images/" + card.image);
    } else {
        e.src = "./images/" + card.image;
    }
    e.style.width = "60px";
    e.style.padding = "2px";
    e.id = "card" + card.suite + "_" + card.number;
    e.setAttribute("data-suite", card.suite);
    e.setAttribute("data-number", card.number);
    return e;
}

function Card_CreateDeck() {
    var cards = [
        {suite: "H", number: 2, image: "heart_2.png"},
        {suite: "H", number: 3, image: "heart_3.png"},
        {suite: "H", number: 4, image: "heart_4.png"},
        {suite: "H", number: 5, image: "heart_5.png"},
        {suite: "H", number: 6, image: "heart_6.png"},
        {suite: "H", number: 7, image: "heart_7.png"},
        {suite: "H", number: 8, image: "heart_8.png"},
        {suite: "H", number: 9, image: "heart_9.png"},
        {suite: "H", number: 10, image: "heart_10.png"},
        {suite: "H", number: 11, image: "heart_jack.png"},
        {suite: "H", number: 12, image: "heart_queen.png"},
        {suite: "H", number: 13, image: "heart_king.png"},
        {suite: "H", number: 14, image: "heart_1.png"},

        {suite: "D", number: 2, image: "diamond_2.png"},
        {suite: "D", number: 3, image: "diamond_3.png"},
        {suite: "D", number: 4, image: "diamond_4.png"},
        {suite: "D", number: 5, image: "diamond_5.png"},
        {suite: "D", number: 6, image: "diamond_6.png"},
        {suite: "D", number: 7, image: "diamond_7.png"},
        {suite: "D", number: 8, image: "diamond_8.png"},
        {suite: "D", number: 9, image: "diamond_9.png"},
        {suite: "D", number: 10, image: "diamond_10.png"},
        {suite: "D", number: 11, image: "diamond_jack.png"},
        {suite: "D", number: 12, image: "diamond_queen.png"},
        {suite: "D", number: 13, image: "diamond_king.png"},
        {suite: "D", number: 14, image: "diamond_1.png"},

        {suite: "C", number: 2, image: "club_2.png"},
        {suite: "C", number: 3, image: "club_3.png"},
        {suite: "C", number: 4, image: "club_4.png"},
        {suite: "C", number: 5, image: "club_5.png"},
        {suite: "C", number: 6, image: "club_6.png"},
        {suite: "C", number: 7, image: "club_7.png"},
        {suite: "C", number: 8, image: "club_8.png"},
        {suite: "C", number: 9, image: "club_9.png"},
        {suite: "C", number: 10, image: "club_10.png"},
        {suite: "C", number: 11, image: "club_jack.png"},
        {suite: "C", number: 12, image: "club_queen.png"},
        {suite: "C", number: 13, image: "club_king.png"},
        {suite: "C", number: 14, image: "club_1.png"},

        {suite: "S", number: 2, image: "spade_2.png"},
        {suite: "S", number: 3, image: "spade_3.png"},
        {suite: "S", number: 4, image: "spade_4.png"},
        {suite: "S", number: 5, image: "spade_5.png"},
        {suite: "S", number: 6, image: "spade_6.png"},
        {suite: "S", number: 7, image: "spade_7.png"},
        {suite: "S", number: 8, image: "spade_8.png"},
        {suite: "S", number: 9, image: "spade_9.png"},
        {suite: "S", number: 10, image: "spade_10.png"},
        {suite: "S", number: 11, image: "spade_jack.png"},
        {suite: "S", number: 12, image: "spade_queen.png"},
        {suite: "S", number: 13, image: "spade_king.png"},
        {suite: "S", number: 14, image: "spade_1.png"}
    ];
    return cards;
}

function CPUPlayer_createCPUPlayer() {
    var p = {...CPUPlayer};
    p.cards = [];
    return p;
}

var Plump = {
    round: 0,
    player: null,
    showedPlayerPlump: false,
    showedCPUPlump: false,
    cpu: null,
    deck: null,
    points: [
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]]
    ],
    startingPlayer: null
};

function Plump_GetNumberOfCardsForRound(round) {
    if (round < 10)
        return 10+1-round;
    if (round < 20)
        return round+1-10;
    else
        return 10;
}

function GetRandomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function Card_ShuffleDeck(deck) {
    var shuffledCards = [];
    for (var i = 0; i < deck.length; i++) {
        var newPosition = -1;
        while (newPosition == -1 || shuffledCards[newPosition] != null)
            newPosition = GetRandomInteger(0, 51);
        var c = deck[i];
        shuffledCards[newPosition] = c;
    }

    deck.length = 0;

    for (var i = 0; i < shuffledCards.length; i++) {
        deck.push(shuffledCards[i]);
    }
}

function Card_DealCards(deck, player, n) {
    for (var i = 0; i < n; i++)
        player.cards.push(deck.pop());
}

function Plump_CPUPlayCard(p, playerCard) {
    var playableCards = [];
    if (playerCard != null) {
        for (var i = 0; i < p.cpu.cards.length; i++) {
            var c = p.cpu.cards[i];
            if (c.suite == playerCard.suite)
                playableCards.push(c);
        }
    }
    if (playableCards.length == 0)
        playableCards = p.cpu.cards;
    return p.cpu.cards.pop(GetRandomInteger(0, p.cpu.cards.length-1));
}

function GUI_MakePlayerCardsPlayableByClicking(playableCards, playedCallback) {
    var e = document.querySelector("#player-area");
    e.onclick = function(event) {
        if (event.target.id == "player-area") return;
        var c = event.target;
        var card = {suite: c.getAttribute("data-suite"), number: Number(c.getAttribute("data-number"))};
        var clickedCardIsPlayable = false;
        for (var i = 0; i < playableCards.length; i++) {
            if (Card_IsSameCard(playableCards[i], card))
                clickedCardIsPlayable = true;
        }
        if (!clickedCardIsPlayable)
            return;

        GUI_PlayPlayerCardByClick(event.target);
        setTimeout(function() {
            playedCallback({suite: c.getAttribute("data-suite"), number: Number(c.getAttribute("data-number"))});
        }, 1000);
    }
}

function GUI_HidePlump() {
    var e = document.querySelector("#plump");
    e.style.display = "none";
}

function GUI_HideChooseSticks() {
    var e = document.querySelector("#choose-sticks");
    e.style.display = "none";
}

function GUI_ShowChooseSticks(p, cpuSticks, ok_callback) {
    var s = document.querySelector("#choose-sticks-round");
    s.innerHTML = "Round " + p.round + "/20";
    var e = document.querySelector("#choose-sticks");
    e.style.display = "";
    var c = document.querySelector("#cpu-selected-sticks");
    if (cpuSticks != null) {
        c.innerText = "CPU selected " + cpuSticks + " sticks.";
    } else {
        c.style.display = "none";
    }
    var i = e.querySelector("input");
    i.focus();
    var b = e.querySelector("button");
    b.onclick = function() {
        var n = Number(i.value);
        if (isNaN(n)) return;
        if (n < 0 || n > 10) return;
        if (!Plump_PlayerChooseSticks(p, n, cpuSticks)) return;
        ok_callback(i.value);
    }
}

function Plump_PlayerChooseSticks(p, sticks, cpuSticks) {
    if (cpuSticks != null && Plump_GetNumberOfCardsForRound(p.round) == (sticks + cpuSticks))
        return false;
    else if (sticks > Plump_GetNumberOfCardsForRound(p.round))
        return false;
    p.points[p.round-1][0][0] = Number(sticks);
    return true;
}

function Plump_CPUChooseSticks(p, opposingSticks, maxSticks) {
    var sticks = 0;
    for (const c of p.cpu.cards) {
        if (c.number > 8)
            sticks++;
    }
    if (opposingSticks == null) {
        ;
    } else if (opposingSticks > 4) {
        sticks = Math.floor(sticks / 2);
    } else if (opposingSticks == 0) {
        while (sticks < maxSticks)
            sticks++;
    }

    if (opposingSticks != null && opposingSticks + sticks == maxSticks)
        sticks--;

    if (sticks < 0)
        sticks = sticks + 2;

    p.points[p.round-1][1][0] = sticks;
    return sticks;
}

function Plump_GetStartingPlayer(p) {
    if (p.points[p.round-1][0][0] > p.points[p.round-1][1][0])
        return p.player;
    else if (p.points[p.round-1][0][0] == p.points[p.round-1][1][0])
        return p.startingPlayer;
    else
        return p.cpu;
}

function GUI_ClearPlayArea() {
    var e = document.querySelector("#play-area");
    e.innerHTML = "";
}

function Card_WinningCard(c1, c2) {
    if (c2.suite == c1.suite && c2.number > c1.number) {
        return c2;
    } else {
        return c1;
    }
}

function GUI_HideStickFinished() {
    var e = document.querySelector("#stick-finished");
    e.style.display = "none";
}

function GUI_ShowStickFinished(playerWins, onHide) {
    var e = document.querySelector("#stick-finished");
    e.style.display = "";
    if (playerWins == false)
        e.innerText = "You lost the stick.";
    else
        e.innerText = "You won the stick.";
    setTimeout(function() {
        e.style.display = "none";
        onHide();
    }, 2000);
}

function Card_IsSameCard(c1, c2) {
    return (c1.suite == c2.suite && c1.number == c2.number);
}

function GUI_ShowPlump(p, onHide) {
    var e = document.querySelector("#plump");
    e.style.display = "";
    e.innerText = "";
    if (p.player.plump)
        e.innerText = "You made plump. ";
    else if (p.cpu.plump)
        e.innerText = "CPU made plump.";
    else if (p.player.plump && p.cpu.plump)
        e.innerText = "Both made plump.";
    setTimeout(function() {
        e.style.display = "none";
        onHide();
    }, 2000);
}

function Card_RemovePlayerCard(p, playerCard) {
    var i = null;
    for (var i = 0; i < p.player.cards.length; i++) {
        var c = p.player.cards[i];
        if (Card_IsSameCard(c, playerCard)) {
            p.player.cards.splice(i, 1);
        }
    }
}

function GUI_UpdateScore(p) {
    var e = document.querySelector("#player-score-taken-sticks");
    e.innerHTML = p.points[p.round-1][0][1];
    var e = document.querySelector("#cpu-score-taken-sticks");
    e.innerHTML = p.points[p.round-1][1][1];
}

function GUI_ClearAllCards() {
    var e = document.querySelector("#player-area");
    e.innerHTML = "";
    var e = document.querySelector("#cpu-area");
    e.innerHTML = "";
}

function GUI_HideFinalScore() {
    var e = document.querySelector("#final-score"); 
    e.style.display = "none";
}

function GUI_ShowFinalScore(p) {
    var e = document.querySelector("#final-score"); 
    e.style.display = "";

    var playerScore = 0, cpuScore = 0;
    for (var i = 0; i < 20; i++) {
        playerScore += p.points[i][0][2];
        cpuScore += p.points[i][1][2];
    }
    e.innerText = "The game is finished! Your score is " + playerScore + ". The CPU scored " + cpuScore + ".";
}

function Plump_IncreaseScore(p, player) {
    if (p.player == player)
        p.points[p.round-1][0][1]++;
    else
        p.points[p.round-1][1][1]++;
}

function Plump_GetPlayerPlayableCards(p, cpuCard) {
    var playableCards = [];
    for (var i = 0; i < p.player.cards.length; i++) {
        var c = p.player.cards[i];
        if (c.suite == cpuCard.suite)
            playableCards.push(c);
    }
    if (playableCards.length == 0)
        return p.player.cards;
    return playableCards;
}

function Plump_PlayRound(p, round) {
    p.showedPlayerPlump = false;
    p.showedCPUPlump = false;
    p.round = round;
    GUI_UpdateScore(p);
    p.player.cards = [];
    p.cpu.cards = [];
    p.deck = Card_CreateDeck();
    p.player.plump = false;
    p.cpu.plump = false;

    if (p.startingPlayer == this.player)
        p.startingPlayer = this.cpu;

    GUI_ClearAllCards(p);

    Card_ShuffleDeck(p.deck);
    var numberOfCards = Plump_GetNumberOfCardsForRound(round);
    Card_DealCards(p.deck, p.player, numberOfCards);
    GUI_DealCards("player", p.player.cards, false);
    Card_DealCards(p.deck, p.cpu, numberOfCards);
    GUI_DealCards("cpu", p.cpu.cards, true);

    function onRoundFinished() {
        if (p.points[round-1][0][0] == p.points[round-1][0][1])
            p.points[round-1][0][2] = p.points[round-1][0][0] + 10;

        if (p.points[round-1][1][0] == p.points[round-1][1][1])
            p.points[round-1][1][2] = p.points[round-1][1][0] + 10;

        GUI_Scoreboard_AddScore("player", p.points[round-1][0][2]);
        GUI_Scoreboard_AddScore("cpu", p.points[round-1][1][2]);

        if (p.round == 20)
            GUI_ShowFinalScore(p);
        else
            Plump_PlayRound(p, round+1);
    }

    var cardsPlayed = 0;
    function onCardsSelected(playerCard, cpuCard) {
        if (cardsPlayed == numberOfCards)
            return;

        var winningCard;
        if (p.startingPlayer == p.player)
            winningCard = Card_WinningCard(playerCard, cpuCard);
        else
            winningCard = Card_WinningCard(cpuCard, playerCard);

        if (Card_IsSameCard(winningCard, playerCard)) {
            Plump_IncreaseScore(p, p.player);
            p.startingPlayer = p.player;
        } else {
            Plump_IncreaseScore(p, p.cpu);
            p.startingPlayer = p.cpu;
        }

        GUI_UpdateScore(p);
        GUI_ShowStickFinished(winningCard == playerCard, function() {
            GUI_ClearPlayArea();
            
            if (p.points[round-1][0][1] > p.points[round-1][0][0])
                p.player.plump = true;

            if (p.points[round-1][1][1] > p.points[round-1][1][0])
                p.cpu.plump = true;

            function onCardsPlayed() {
                if ((p.cpu.plump && p.player.plump) || p.player.cards.length == 0) {
                    onRoundFinished();
                } else {
                    onSticksPicked(false);
                }
            }

            if (p.cpu.plump || p.player.plump)
                if (p.player.plump && p.showedPlayerPlump == false) {
                    p.showedPlayerPlump = true;
                    GUI_ShowPlump(p, function() {
                        onCardsPlayed();
                    });
                }

                if (p.cpu.plump && p.showedCPUPlump == false) {
                    p.showedCPUPlump = true;
                    GUI_ShowPlump(p, function() {
                        onCardsPlayed();
                    });
                }
            else
                onCardsPlayed();
        });
    }


    function onSticksPicked(firstStick) {
        if (firstStick)
            p.startingPlayer = Plump_GetStartingPlayer(p);

        if (p.startingPlayer == p.player) {
            GUI_MakePlayerCardsPlayableByClicking(p.player.cards, function(playerCard) {
                Card_RemovePlayerCard(p, playerCard);
                var cpuCard = Plump_CPUPlayCard(p, playerCard);
                GUI_PlayCard("cpu", cpuCard, function() {
                    onCardsSelected(playerCard, cpuCard);
                });
            });
        } else {
            var cpuCard = Plump_CPUPlayCard(p, null);
            GUI_PlayCard("cpu", cpuCard, function() {});
            var playableCards = Plump_GetPlayerPlayableCards(p, cpuCard);
            GUI_MakePlayerCardsPlayableByClicking(playableCards, function(playerCard) {
                Card_RemovePlayerCard(p, playerCard);
                onCardsSelected(playerCard, cpuCard);
            });
        }
    }
    
    if (p.startingPlayer == p.player) {
        GUI_ShowChooseSticks(p, null, function(playerSticks) {
            var cpuSticks = Plump_CPUChooseSticks(p, playerSticks, numberOfCards);
            GUI_HideChooseSticks();

            GUI_Score_SetScore("cpu", cpuSticks, 0);
            GUI_Score_SetScore("player", playerSticks, 0);
            onSticksPicked(true);
        });
    } else {
        var cpuSticks = Plump_CPUChooseSticks(p, null, numberOfCards);
        GUI_ShowChooseSticks(p, cpuSticks, function(playerSticks) {
            GUI_HideChooseSticks();

            GUI_Score_SetScore("cpu", cpuSticks, 0);
            GUI_Score_SetScore("player", playerSticks, 0);
            onSticksPicked(true);
        });
    }

}

function Plump_PlayGame() {
    GUI_Score_SetScore("cpu", 0, 0);
    GUI_Score_SetScore("player", 0, 0);
    GUI_Scoreboard_Clear();

    var p = {...Plump};
    PlumpGame = p;
    p.player = Player_createPlayer();
    p.player.number = 0;
    p.cpu = CPUPlayer_createCPUPlayer();
    p.cpu.number = 1;
    p.deck = Card_CreateDeck();
    p.startingPlayer = p.cpu;  // Make player start.
    Plump_PlayRound(p, 1);
}

window.onload = function() {
    GUI_HidePlump();
    GUI_HideChooseSticks();
    GUI_HideStickFinished();
    GUI_HideFinalScore();
    GUI_CreateMenu();
    
};
