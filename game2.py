import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as list
        self.human = 'X'
        self.computer = 'O'
        self.current_player = self.human
    
    def display_board(self):
        """Display the current board state"""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")
    
    def display_board_with_numbers(self):
        """Display board with position numbers for player guidance"""
        print("\nPilihan posisi:")
        print(f" 1 | 2 | 3 ")
        print("-----------")
        print(f" 4 | 5 | 6 ")
        print("-----------")
        print(f" 7 | 8 | 9 ")
        print("\n")
    
    def is_winner(self, player):
        """Check if the specified player has won"""
        # Define all winning combinations
        win_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal top-left to bottom-right
            [2, 4, 6]   # Diagonal top-right to bottom-left
        ]
        
        for combination in win_combinations:
            if all(self.board[i] == player for i in combination):
                return True
        return False
    
    def is_board_full(self):
        """Check if the board is full"""
        return ' ' not in self.board
    
    def get_available_moves(self):
        """Get list of available positions"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_smart_move(self):
        """Computer makes a smart move using simple strategy"""
        available = self.get_available_moves()
        
        # First, try to win
        for move in available:
            self.board[move] = self.computer
            if self.is_winner(self.computer):
                return move
            self.board[move] = ' '
        
        # Second, block player from winning
        for move in available:
            self.board[move] = self.human
            if self.is_winner(self.human):
                self.board[move] = ' '
                return move
            self.board[move] = ' '
        
        # Third, prefer center
        if 4 in available:
            return 4
        
        # Fourth, prefer corners
        corners = [0, 2, 6, 8]
        corner_moves = [move for move in available if move in corners]
        if corner_moves:
            return random.choice(corner_moves)
        
        # Finally, choose any available move
        return random.choice(available)
    
    def player_move(self):
        """Get player input and make a move"""
        while True:
            try:
                position = input("Pilih posisi (1-9): ")
                pos = int(position) - 1
                
                if pos < 0 or pos > 8:
                    print("Posisi harus antara 1-9!")
                    continue
                
                if self.board[pos] != ' ':
                    print("Posisi sudah terisi!")
                    continue
                
                self.board[pos] = self.human
                break
            except ValueError:
                print("Input tidak valid! Masukkan angka 1-9.")
    
    def computer_move(self):
        """Computer makes a move"""
        move = self.make_smart_move()
        self.board[move] = self.computer
        print(f"Komputer memilih posisi: {move + 1}")
    
    def play(self):
        """Main game loop"""
        print("=" * 30)
        print("  SELAMAT DATANG DI TIC TAC TOE")
        print("=" * 30)
        print("\nAnda bermain sebagai X")
        print("Komputer bermain sebagai O")
        
        self.display_board_with_numbers()
        
        while True:
            self.display_board()
            
            # Player move
            print("Giliran Anda (X):")
            self.player_move()
            
            # Check if player won
            if self.is_winner(self.human):
                self.display_board()
                print("🎉 SELAMAT! ANDA MENANG!")
                break
            
            # Check if board is full
            if self.is_board_full():
                self.display_board()
                print("🤝 PERMAINAN SERI (DRAW)!")
                break
            
            # Computer move
            print("\nGiliran Komputer (O):")
            self.computer_move()
            
            # Check if computer won
            if self.is_winner(self.computer):
                self.display_board()
                print("😢 KOMPUTER MENANG! COBA LAGI!")
                break
            
            # Check if board is full
            if self.is_board_full():
                self.display_board()
                print("🤝 PERMAINAN SERI (DRAW)!")
                break
        
        print("=" * 30)
    
    def reset(self):
        """Reset the game for a new round"""
        self.board = [' ' for _ in range(9)]
        self.current_player = self.human


def main():
    """Main function to run the game"""
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("\nIngin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            print("\nTerima kasih telah bermain! Sampai jumpa!")
            break


if __name__ == "__main__":
    main()
