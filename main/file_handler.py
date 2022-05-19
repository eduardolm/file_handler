import re


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

    #  ************************  With REGEX  *****************************

    def separate_data(self) -> tuple:
        host_pattern = r'[\d]+\.[\d]+\.[\d]+\.[\d]+'
        user_pattern = r'-\s([A-Za-z0-9_-]+)\s'
        time_pattern = r'\[[\d].+[\d]\]'
        request_pattern = r'["].+["]'

        hosts = re.findall(host_pattern, self.log_data)
        user = re.findall(user_pattern, self.log_data)
        time = re.findall(time_pattern, self.log_data)
        request = re.findall(request_pattern, self.log_data)

        return hosts, user, time, request

    def build_regex_final_response(self):
        response = []
        data = self.separate_data()
        for i in range(len(data[0])):
            output = {
                'host': data[0][i],
                'user_name': data[1][i],
                'time': data[2][i],
                'request': data[3][i]
            }
            response.append(output)

        return response
