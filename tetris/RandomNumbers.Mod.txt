MODULE RandomNumbers;

IMPORT SYSTEM;

CONST
	timer = -64;

(* Park-Miller 1993 *)
	a = 48271; m = 7FFFFFFFH; q = m DIV a; r = m MOD a;


VAR z*: INTEGER;

PROCEDURE Time(): LONGINT;
	VAR msec: LONGINT; BEGIN SYSTEM.GET(timer, msec); RETURN msec END Time;

PROCEDURE Uniform*(): REAL; (* returns a random nbr 0 < x < 1 *)
	(*   z = a * z MOD m   by Schrage's method *)
	BEGIN
		z := a*(z MOD q) - r*(z DIV q);
		IF z < 0 THEN INC(z, m) END
	RETURN FLT(z) / FLT(m)
	END Uniform;

PROCEDURE RND*(max: INTEGER): INTEGER;	(* returns an integer in the range 0..max-1 *)
	RETURN FLOOR(Uniform() * FLT(max))
	END RND;

PROCEDURE InitSeed*(seed: INTEGER);
	BEGIN
		IF seed = 0 THEN z := 1 ELSE z := seed END;
	END InitSeed;

BEGIN
	InitSeed(Time())
END RandomNumbers.

(*
ORP.Compile RandomNumbers.Mod/s ~
System.Free RandomNumbers ~
*)
