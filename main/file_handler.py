class FileHandler:
    log_data: str

    def build_final_response(self) -> list:
        response = []
        for item in self.split_items():
            output = {
                    'host': item[0],
                    'user_name': item[2],
                    'time': f'{item[3]} {item[4]}',
                    'request': f'{item[5]} {item[6]} {item[7]}'
                }
            response.append(output)
        return response

    def split_items(self) -> list:
        response = []
        for item in self.extract_lines():
            response.append(item.split(' '))

        return response

    def extract_lines(self) -> list:
        response = self.log_data.split('\n')
        response.pop()

        return response

    def read_file(self, path: str) -> str:
        with open(path, 'r') as fp:
            self.log_data = fp.read()

        return self.log_data
