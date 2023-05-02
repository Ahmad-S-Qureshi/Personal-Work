#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Define the structure for a DOS card
typedef struct card_s {
  char color[10];
  int value;
  char action[15];
  struct card_s *next;
} card;

// Define the structure for a player
typedef struct player_s {
  card *hand[7];
  int is_out;
} player;

// Function to initialize a new card
card *new_card() {
  card *new_card = malloc(sizeof(card));
  new_card->color[0] = '\0';
  new_card->value = 0;
  new_card->action[0] = '\0';
  new_card->next = NULL;
  return new_card;
}

// Function to shuffle the deck of cards
void shuffle_deck(card *deck[]) {
  int i, j;
  card *temp;
  for (i = 0; i < 108; i++) {
    j = rand() % 108;
    temp = deck[i];
    deck[i] = deck[j];
    deck[j] = temp;
  }
}

// Function to deal the cards to the players
void deal_cards(card *deck[], player players[]) {
  int i, j;
  for (i = 0; i < 7; i++) {
    for (j = 0; j < 2; j++) {
      players[j].hand[i] = deck[i];
      deck[i] = deck[107];
      deck[107] = NULL;
    }
  }
  return;
}

// Function to check if a player can play a card
int can_play_card(player *player, card *card) {
  if (card->color[0] == '\0') {
    return 1;
  } else if (card->color[0] == player->hand[0]->color[0]) {
    return 1;
  } else if (card->value == player->hand[0]->value) {
    return 1;
  } else if (strcmp(card->action, "multi-color 2")  == 0) {
    return 1;
  }
  return 0;
}

// Function to play a card
void play_card(player* player, card* card) {
  card temp = new_card()
  temp = player->hand[0];
  player->hand[0] = card;
  card = temp;
  card->next = NULL;
  if (player->hand[0] == NULL) {
    player->is_out = 1;
  }
}