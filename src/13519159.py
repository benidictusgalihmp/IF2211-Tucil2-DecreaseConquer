# Membaca input dari file .txt dengan parameter string
def readFile(filename):
    # inisialisasi list kosong
    graph = []

    # membuka file .txt dan menyimpannya dalam variabel f
    with open('../test/'+filename+'.txt', 'r') as f:

        # Memasukan input dari file ke dalam array files dengan pembeda newline
        files = f.read().splitlines()

        for i in range(len(files)):
            files[i] = files[i].replace(',','')     # mereplace tanda koma dengan kosong
            files[i] = files[i].replace('.','')     # mereplace tanda titik dengan kosong
            files[i] = files[i].split()

            # memasukan array files ke dalam array graph (2D array)
            graph.append(files[i])
            
        f.close()       # menutup file

    return graph

# menghapus elemen array
def deletematkul(temp_graph, matkul):
    # inisialisasi increment
    i = 0
    
    # looping array x
    while(i < len(temp_graph)):

        # looping array y dalam array x
        # temp_matkul isi dari array y
        for temp_matkul in temp_graph[i]:

            if(temp_matkul == matkul):
                temp_graph[i].remove(temp_matkul)   # meremove elemen dari array
        i += 1

    # end loop while

    return temp_graph

# menghapus array kosong
def deletelistkosongmatkul(temp_graph):
    # inisialisasi increment dan update init_length
    init_length = len(temp_graph)
    i = 0

    while(i < init_length):

        # jika panjang elemen array y = 0, maka array tersebut dihapus
        # nilai init_length diupdate supaya tidak infinite loop
        if(len(temp_graph[i]) == 0):
            temp_graph.remove(temp_graph[i])
            init_length = len(temp_graph)
        else:
            i += 1
    # end loop while

    return temp_graph

# mengembalikan nilai boolean jika menemukan ada list dengan panjang array = 1
def isSearcOneListhMatkul(temp_graph):
    # inisialisasi increment dan boolean
    found = False
    i = 0

    while(not found and i < len(temp_graph)):
        # bool bernilai true jika panjang array = 1 dan isi array tidak kosong
        if(len(temp_graph[i]) == 1 and temp_graph[i] != ""):
            found = True
        else:
            i += 1
    # end loop while

    return found

# mengembalikan nilai elemen dari array graph yang panjang arraynya = 1
def searchOneListMatkul(temp_graph):
    # inisialisasi increment dan boolean
    found = False
    i = 0

    while(not found and i < len(temp_graph)):
        if(len(temp_graph[i]) == 1):
            found = True
        else:
            i += 1
    # end loop while
    # nilai i = nilai indeks dari alamat array elemen yang dicari berada

    return temp_graph[i][0]

# rekursif dengan memanggil kembali graph yang telah diremove 
# parameter berupa graph
# dan idx sebagai index dari array semester
def sortingGraph(temp_graph, idx):
    
    # basis dari rekursif ketika array sudah kosong
    if(len(temp_graph) == 0):
        return 0
    
    # basis dari rekursif ketika panjang array = 1, 
    # nilai elemen diappend ke array baru bernama semester.
    # Hapus juga matkul yang diambil tadi dan remove list kosong
    elif(len(temp_graph) == 1):
        semester[idx - 1].append(searchOneListMatkul(temp_graph))
        deletematkul(temp_graph, searchOneListMatkul(temp_graph))
        deletelistkosongmatkul(temp_graph)

    # panjang array lebih dari 1
    else:

        # Pencarian apakah terdapat list dengan panjang array = 1
        # jika ada, elemen akan di append ke array semester
        # elemen dihapus dari array graph dan array dihapus
        while(isSearcOneListhMatkul(temp_graph)):
            semester[idx - 1].append(searchOneListMatkul(temp_graph))
            deletematkul(temp_graph, searchOneListMatkul(temp_graph))
            deletelistkosongmatkul(temp_graph)
            idx += 1
        # end loop while

        # pemanggilan rekursif
        sortingGraph(temp_graph, idx)

def printRencanaKuliah(temp_graph):
    # inisialisasi increment dan bool while pertama
    i = 0
    end1 = False

    print()
    print("Rencana kuliah: ")

    while(not end1 and i < len(temp_graph)):

        # inisialisasi increment dan bool while kedua
        end2 = False
        j = 0

        if(temp_graph[i] != []):
            # output semester ke berapa berdasarkan nilai i (alamat array)
            print("Semester", i + 1,": ", end="")

            while (not end2 and j < len(temp_graph[i])):
                if(temp_graph[i] != []):
                    if(j == len(temp_graph[i]) - 1):
                        print(temp_graph[i][j], end="")
                    else:
                        print(temp_graph[i][j], end=", ")
                    j += 1

                else:   # ada elemen kosong
                    end2 = True

            i += 1
            print()         # enter

            # end loop while kedua
        else:
            end1 = True
    # end loop while pertama

# main algoritma

# inisialisasi array semester dengan panjang array 50
semester = [[] for i in range(50)]

# meminta input nama file testing dari user
filename = str(input("Masukkan nama file: "))

# memanggil fungsi readFile dengan parameter string
test_file = readFile(filename)

# memanggil rekursif topological sorting
sortingGraph(test_file, 1)

# mengeluarkan output ke layar berdasarkan hasil rekursif
printRencanaKuliah(semester)