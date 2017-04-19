# Computor_V1
42 - Project #09

Ecrivez un programme qui résout une équation polynomiale de degré inférieur ou e´gal
à 2. Vous devrez afficher au moins :<br>
• La forme réduite de l’équation.<br>
• Le degré de l’équation.<br>
• Sa ou ses solution(s), ainsi que le signe du discriminant quand cela a du sens.

--------------------------------------------------------------------------------

Exemples :<br>
$>./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"<br>
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0<br>
Polynomial degree: 2<br>
Discriminant is strictly positive, the two solutions are:<br>
0.905239<br>
-0.475131<br>
$>./computor "5 * X^0 + 4 * X^1 = 4 * X^0"<br>
Reduced form: 1 * X^0 + 4 * X^1 = 0<br>
Polynomial degree: 1<br>
The solution is: -0.25<br>
./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"<br>
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0<br>
Polynomial degree: 3<br>
The polynomial degree is stricly greater than 2, I can't solve.<br>

--------------------------------------------------------------------------------

On considèrera toujours que l’entrée est bien formatée, ie. tous les termes sont de la
forme a ∗ xp. Les puissances sont bien ordonnées et toutes présentes. Attention, cela ne
signifie pas forcement que l’équation soit soluble ! Dans ce cas, votre programme doit le
détecter et l’indiquer. Pensez aussi aux coefficients nuls, négatifs, pas entiers ...
Il existe peut-être des cas particuliers que vous devez gérer. Par exemple pour l’équation
42 ∗ X0 = 42 ∗ X0, tous les nombres réels sont solution...
