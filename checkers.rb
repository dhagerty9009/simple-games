# simple-games.checkers, written by David Hagerty
# Copyright 2011, licenced under the GPL
#
# The goal of checkers is to eliminate all of your opponent's pieces
# You can only move diagonally forward, unless the piece is a king.
# Player pieces will be denoted by the letter "P", kings by "PK"
# Computer pieces will be denoted by "C", kings by "CK"

def getPlayerColor()
  player_choice = ""
  while player_choice != "B" or player_choice != "W"
    puts "What color do you want to be?"
    puts "Black (B)? Or White (W)?"
    player_choice = gets.chomp.capitalize
    if player_choice == "B"
      computer_choice = "W"
      break
    else player_choice == "W"
      computer_choice = "B"
      break
    end
  end
  return player_choice, computer_choice
end

# Here is the main game logic
puts "Welcome to the game of checkers!"
puts "Please choose your color."
player_color, computer_color = getPlayerColor()
puts "Your pieces are marked by "+player_color+"s."
puts "The computer's pieces are marked by "+computer_color+"s"
