# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""

from pypacman.ai import *


"""
Teste do Astar
"""

"""
Grade do jogo
"""

G = [
"###..####################..####################..####################..####################..#################.",
".........*........#.#..........*........#.#...........*........#.#...........*........#.............*.......#..",
"....#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####........#....#.##.###..",
"#...#....#..#**....*..#...#....#..#......*..#...#....#..#......*..#...#....#..#......*......#....#..#......*...",
"#.####...#*##+*....*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.#.",
"#....#..##..***....#.##....#..##.........#.##....#..##.........#.##....#..##.........#.##..................#.#.",
"#....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####........#.###.##..###.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#...............##............#..#....#.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.............................#..#....#.",
"###..#.##########.#######..#.##########.#######..#.##########.#######..#.##########.##.####..#.##########.####.",
"#...##.....#....#.#.......##.....#....#.#..##...##.....#....#.#.......##.....#....#.#.......##.....#....#.#..#.",
"#..........#.....................#.........##..........#.....................#.........##..........#.........#.",
"###..#.....##############..#.....##############..#.....##############..#.....#########.####..#.....######..###.",
".........*.....................*......................*........#.#...........*..........#...........*.......#..",
"....#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####.#......#....#.##..##..",
"#...#....#..#......*..#...#....#..#......*..#...#....#..#......*...........#..#......*..#...#....#..#......*...",
"#.####...#*##......*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.#.",
"#....#..##.........#.##....#..##.........#.##....#..##.........#.##....#..##.........#.......#..##.........#.#.",
"#....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####....#...#.###.##..###.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.......#..#....##............#..#....#.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.......#..#....#.",
"###..#.##########.#######..#.##########.#######..#.##########.#######..#.##########.#######..#.##########.####.",
"#...##.....#....#.#..##...##.....#....#.#..##...##.....#....#.#..##...##.....#....#.#..##...##.....#....#.#..#.",
"#..........#.........##..........#.........##..........#.........##..........#.........##..........#.........#.",
"###..#.....##############..#.....##############..#.....##############..#.....##############..#.....###########.",
"....x.........................................................................................................."];

"""
Possibilidades de movimentação:
...
.x.
...
"""

dx = [-1,  0,  0,  1];
dy = [ 0, -1,  1,  0];

res = a_star.a_star(G, dx, dy);

D = res['D'];
s = res['s'];
t = res['t'];
pi = res['pi'];
u = res['u'];

if D[t[0]][t[1]] != None:
	print "A distância entre s e t é: ", D[t[0]][t[1]]; 
	"""
	Descomente essa linha caso queira ver a sequencia de passos percorrido pelo jogador
	"""
	#a_star.imprime_caminho(pi, t);
	"""
	Descomente essa linha se quiseres ver o caminho percorrido na grade
	"""
	#a_star.renderizar_caminho(pi, G, u);
	caminho = []
	a_star.gera_caminho(caminho, pi, u);
	print "caminho: ";
	print caminho;
	print "s: " 
	print s;
	print "t: ";
	print t;
else:
	print "Não existe caminho entre s e t!"

