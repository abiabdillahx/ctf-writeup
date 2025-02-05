import socket
import re

def solve_math_problem(problem):
    try:
        # Menggunakan eval langsung tanpa mengganti '//' dengan '/'
        return eval(problem)
    except ZeroDivisionError:
        return None


def main():
    host = "34.66.235.106"
    port = 5000

    # Membuat koneksi ke server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Membaca dan menyelesaikan pertanyaan
        while True:
            data = s.recv(1024).decode()
            if not data:
                break
            
            print(data)

            # Mencari persamaan matematika
            match = re.search(r'Question: ([-+*//\d\s]+)', data)
            if match:
                problem = match.group(1).strip()
                print(f"Solving: {problem}")
                
                # Menyelesaikan persamaan
                answer = solve_math_problem(problem)
                if answer is not None:
                    s.sendall(f"{int(answer)}\n".encode())
                else:
                    print("Zero division error occurred.")
                    break

            # Mencetak flag jika ditemukan
            if "Congratz!" in data:
                print(data)
                break

if __name__ == "__main__":
    main()
