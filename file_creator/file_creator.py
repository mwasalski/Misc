#To Do:
# błąd, jeśli pliki już istnieją, żeby nie nadpisywać
# print do parqueta


class file_creator:
    def __init__(self, folder = None, files = None, extensions = None):

        # parametry do metod
        self.folder = folder
        self.files = files
        self.extensions = extensions

        # self.os jakbym chciał użyć jakieś innej metody
        import os
        self.os = os
        
        import pandas
        self.pandas = pandas    
        import pyarrow
        self.pyarrow = pyarrow
        import pyarrow.parquet
        self.pyarrow_parquet = pyarrow.parquet


    def create_files_diff_extension(self, folder=None, files=None, extensions=None):
        
        # Use parameters from method if provided, otherwise use instance variables
        folder_path = folder or self.folder
        files = files or self.files
        extensions = extensions or self.extensions

            # jeśli nie podałem folderu:
        if folder is None:
            folder_path = self.os.getcwd() # folder_path to folder w którym jest plik
        else:
            folder_path = folder # jesli podałem, to stworzy folder w folderze, w którym jest plik
               
         # jeżeli podałem folder i on nie istnieje, to go tworzy
        # print(os.path.exists('file.txt')) - sprawdza, czy plik file.txt istnieje
        if folder and not self.os.path.exists(folder_path):
            self.os.makedirs(folder_path)

        # jeśli długość listy files i extensions nie są równe, to wywala błąd
        if len(files) != len(extensions):
            raise ValueError("Dla każdego pliku musisz podać rozszerzenie.")
        
        # Tworzenie plików
        # Zip - łączy ze soba dwa iterowalne obiekty np. listy, tuple, slowniki
        for file, ext in zip(files, extensions):
            # tworzy ścięzkę do pliku: ścieżka.join(folder_path, złączone nazwa pliku i rozszerzenie)
            file_path = self.os.path.join(folder_path, f"{file}.{ext}")
            # tworzy plik (ścieżka, tryb "w" - write, czyli zapisuje)
            with open(file_path, "w") as file:
                file.write("")  # Tworzy pusty plik
        
        return f"Plików: {len(files)}\nFolder: {folder_path}"
    
    def create_file_one_extension(self, folder=None, files=None, extension=None):
        
        # Use parameters from method if provided, otherwise use instance variables
        folder_path = folder or self.folder
        files = files or self.files
        extension = extension or self.extension
        
                    # jeśli nie podałem folderu:
        if folder is None:
            folder_path = self.os.getcwd() # folder_path to folder w którym jest plik
        else:
            folder_path = folder # jesli podałem, to stworzy folder w folderze, w którym jest plik
        
                 # jeżeli podałem folder i on nie istnieje, to go tworzy
        # print(os.path.exists('file.txt')) - sprawdza, czy plik file.txt istnieje
        if folder and not self.os.path.exists(folder_path):
            self.os.makedirs(folder_path)
            
        for file in files:
            ext = extension
             # tworzy ścięzkę do pliku: ścieżka.join(folder_path, złączone nazwa pliku i rozszerzenie)
            file_path = self.os.path.join(folder_path, f"{file}.{ext}")
            # tworzy plik (ścieżka, tryb "w" - write, czyli zapisuje)
            with open(file_path, "w") as file:
                file.write("")  # Tworzy pusty plik
                
        return f"Stworzone pliki: {files}\nFolder: {folder_path}"
    
    
    def create_file_parquet(self, folder=None, data_dict=None):
        
        folder_path = folder or self.folder
        
        # jeśli nie podałem folderu:
        if folder is None:
            folder_path = self.os.getcwd() # folder_path to folder w którym jest plik
        else:
            folder_path = folder # jesli podałem, to stworzy folder w folderze, w którym jest plik
        
        df = self.pandas.DataFrame(data_dict)

        # dataframe to table
        table = self.pyarrow.Table.from_pandas(df)

        # table to parquet_file
        self.pyarrow.parquet.write_table(table,  f'{folder_path}/config_table.parquet')
        
        
# Przykład użycia
folder = "folder"
files = ["plik", "plikk", "plikkk"]
extensions = ["ipynb", "py", "md"]
extension = "mp3"

# dataframe
data = {
'Date': [],
'Name': [],
'Surname': [],
'Country': [],
'Value': []
}

fc = file_creator()
result = fc.create_files_diff_extension(folder, files, extensions)
print(result)


oe = fc.create_file_one_extension(folder, files, extension)
print(oe)

parquet = fc.create_file_parquet(folder, data)
print(parquet)
