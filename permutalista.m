clc; clear;


% Path to the wordlist
mypath = 'D:\Users\Usuario\Documents\GitHub\Replication_Lucketal1996\';
filename = 'words_spanish.mat';
wordlist = importdata([mypath,filename]); 

% Nwords = 360;
Nwords = size(wordlist,1);


% Generar una permutación aleatoria de los índices de la segunda columna
permutationIndices = randperm(Nwords);
% load permutationIndices

% Aplicar la permutación solo a la segunda columna
wordlist_unrelated = wordlist;
wordlist_unrelated(:, 2) = wordlist(permutationIndices, 2);

save([filename(1:end-4),'_unrelated.mat'],"wordlist_unrelated")
save(['permutationIndices.mat'],"permutationIndices")