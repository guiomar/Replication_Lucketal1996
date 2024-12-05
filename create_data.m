function create_data()
% Create a list of data for Luck et al. 1996 Replication #EEGManyLabs
%
% INPUT: 
%  - wordlist
%
% OUTPUT:
% - LuckList. csv
%   * T0, T1, T2
%   * lags: Lags generated, containing:
%         * lagT1: random values between 7 and 10
%         * lagT2: random (1, 3, or 7)
%         * lagEnd: lagT0 + lagT1 + lagT2 = 20
% - distractors.csv
% 
% Authors: Guiomar Niso, Instituto Cajal, 2024

clc; clear;


% Path to the wordlist
mypath = 'D:\Users\Usuario\Documents\GitHub\Replication_Lucketal1996\';
filename = 'words_spanish.mat';
wordlist = importdata([mypath,filename]); 

% Nwords = 360;
Nwords = size(wordlist,1);
Ndistractors = 20*Nwords;


%% T0: Semantic Context
% Create a list of N words for T0
wordT0 = cell(Nwords,1);
for i=1:Nwords
    wordT0{i} = wordlist{i,1};
end

%% T2: Target word
% Create a list of N words for T2
% Fill in with 'X' the word list pairs
totalChars = 7; % Length for each string
fillChar = 'X';
wordT2 = cell(Nwords,1);
for i=1:Nwords
    wordT2{i} = fillWordX(wordlist{i,2}, totalChars, fillChar);
end

%% T1: Numbers
% Generate a random number between 0 and 9
randNum = randi([2, 9],Nwords,1);
% Create a cell array of random strings with the same number repeated
numberT1 = cellstr(repmat(num2str(randNum), 1, totalChars));

%% Generate lags

lags = zeros(Nwords,3);

for i=1:Nwords
    lags(i,:) = generateRandomLags();
end

%% Response T1: odd / even
responseT1 = cell(Nwords,1);
for i=1:Nwords
    if mod(numberT1{i}(1), 2) == 0 
        responseT1{i} ='j'; % even
    else
        responseT1{i} ='f'; % odd
    end
end

%% Response T2: related / non related
responseT2 = cell(Nwords,1);
for i=1:Nwords  
    responseT1{i} ='j'; % related
end

%% SAVE CSV with all the information

headers = {'T0','T2','T1','lagT0','lagT1','lagT2','reponseT1','reponseT2'};

data = [wordT0 wordT2 numberT1 num2cell(lags,size(lags)) responseT1 responseT2];
% Convert cell array to a table with column names
dataTable = cell2table(data, 'VariableNames', headers);
% Export to CSV file
writetable(dataTable, ['LuckList_',filename(1:end-4),'.csv']);


%% List of distractors

totalChars = 7; % Length for each string
ExcludeLetters = 'AEIOU'; % Letters to exclude
headers = {'dist'};
filename_distractors = 'distractors.csv';

% Create a list of N distractors
distractors = cell(Ndistractors,1);
for i=1:Ndistractors
    distractors{i} = generateRandomString(totalChars, ExcludeLetters);
end

% Convert cell array to a table with column names
dataTable = cell2table(distractors, 'VariableNames', headers);
% Export to CSV file
writetable(dataTable, filename_distractors);

end




function newWord = fillWordX(word, totalChars, fillChar)
% FUNCTION newWord = fillWordX(word, totalChars, fillChar)
%
% Generates a new word filled with 'X' (or any other desired char) up to a
% certain length, with a preference of more filling chars at the begining
% when even distribution is not possible
%
% INPUT: 
%  - word: Word to fill
%  - totalChars: total length (number of chars) of the new word
%  - fillChar: char to use for filling, (e.g. 'X')
%
% OUTPUT:
% - newWord: New filled word
% 
% Authors: Guiomar Niso, Instituto Cajal, 2024


% Length of the original word
wordLength = length(word);

% Calculate the number of characters to add before and after the word
charsBefore = ceil((totalChars-wordLength)/ 2);
charsAfter  = floor((totalChars-wordLength)/ 2);

% Create the filled word
newWord = [repmat(fillChar, 1, charsBefore), word, repmat(fillChar, 1, charsAfter)];

end




function lags = generateRandomLags()
% FUNCTION lags = generateRandomLags()
%
% Generates random lags for the replication of Luck et al. 1996
%
% INPUT: 
%  - word: Word to fill
%  - totalChars: total length (number of chars) of the new word
%  - fillChar: char to use for filling, (e.g. 'X')
%
% OUTPUT:
% - lags: Lags generated, containing:
%         * lagT1: random values between 7 and 10
%         * lagT2: random (1, 3, or 7)
%         * lagEnd: lagT0 + lagT1 + lagT2 = 20
% 
% Authors: Guiomar Niso, Instituto Cajal, 2024

% == Generate random values for lagT1 (either 7 or 10)

% Options for lagT1 (7 or 10)
lagT2Options = [7, 10];
% Generate random indices (1 or 2)
numValues = 1;
randomIndices = randi(2, 1, numValues);
% Map indices to possible values
lagT1 = lagT2Options(randomIndices);

% == Generate random values for lagT2 (either1, 3, or 7)

% Options for lagT2 (1, 3, or 7)
lagT2Options = [1, 3, 7];

% Randomly select an index to get a value from lagT2Options
index = randi(length(lagT2Options));
lagT2 = lagT2Options(index);

% == Calculate lagEnd

% Calculate lagEnd to satisfy lagT1 + lagT2 + lagEnd = 20
lagEnd = 20 - lagT1 - lagT2;

lags = [lagT1 lagT2 lagEnd];

end




function randomString = generateRandomString(totalChars, excludeLetters)
% FUNCTION randomString = generateRandomString(StringLength, ExcludeLetters)
%
% Generates a random string of a certain length excluding specific letters
% (without repeting letters)
%
% INPUT: 
%  - totalChars: Length of the string (number of chars)
%  - excludeLetters: Letters to exclude
%
% OUTPUT:
% - randomString: Generated string
% 
% Authors: Guiomar Niso, Instituto Cajal, 2024

% Define the alphabet (A-Z)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

% Remove specific letters from the alphabet
validChars = alphabet(~ismember(alphabet, excludeLetters));

% Randomly select a number of characters without repetition
randomIndices = randperm(length(validChars), totalChars);

% Create the random string
randomString = validChars(randomIndices);

end




