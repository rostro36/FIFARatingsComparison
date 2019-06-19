import psycopg2
import sys

con = None
fout = None

try:
    con = psycopg2.connect(database='postgres',
                           user='postgres',
                           password='test')
    cur = con.cursor()
    f = open('dataout.csv', 'r', encoding='utf-8')
    next(f)
    cur.execute("DROP TABLE IF EXISTS players")
    cur.execute(
        "CREATE TABLE players(Number VARCHAR(255),ID SERIAL PRIMARY KEY,Name VARCHAR(255),Age VARCHAR(255),Photo VARCHAR(255),Nationality VARCHAR(255),Flag VARCHAR(255),Overall VARCHAR(255),Potential VARCHAR(255),Club VARCHAR(255),ClubLogo VARCHAR(255),Value VARCHAR(255),Wage VARCHAR(255),Special VARCHAR(255),PreferredFoot VARCHAR(255),InternationalReputation VARCHAR(255),WeakFoot VARCHAR(255),SkillMoves VARCHAR(255),WorkRate VARCHAR(255),BodyType VARCHAR(255),RealFace VARCHAR(255),Position VARCHAR(255),JerseyNumber VARCHAR(255),Joined1 VARCHAR(255),LoanedFrom VARCHAR(255),ContractValidUntil VARCHAR(255),Height VARCHAR(255),Weight VARCHAR(255),LS VARCHAR(255),ST VARCHAR(255),RS VARCHAR(255),LW VARCHAR(255),LF VARCHAR(255),CF VARCHAR(255),RF VARCHAR(255),RW VARCHAR(255),LAM VARCHAR(255),CAM VARCHAR(255),RAM VARCHAR(255),LM VARCHAR(255),LCM VARCHAR(255),CM VARCHAR(255),RCM VARCHAR(255),RM VARCHAR(255),LWB VARCHAR(255),LDM VARCHAR(255),CDM VARCHAR(255),RDM VARCHAR(255),RWB VARCHAR(255),LB VARCHAR(255),LCB VARCHAR(255),CB VARCHAR(255),RCB VARCHAR(255),RB VARCHAR(255),Crossing VARCHAR(255),Finishing VARCHAR(255),HeadingAccuracy VARCHAR(255),ShortPassing VARCHAR(255),Volleys VARCHAR(255),Dribbling VARCHAR(255),Curve VARCHAR(255),FKAccuracy VARCHAR(255),LongPassing VARCHAR(255),BallControl VARCHAR(255),Acceleration VARCHAR(255),SprintSpeed VARCHAR(255),Agility VARCHAR(255),Reactions VARCHAR(255),Balance VARCHAR(255),ShotPower VARCHAR(255),Jumping VARCHAR(255),Stamina VARCHAR(255),Strength VARCHAR(255),LongShots VARCHAR(255),Aggression VARCHAR(255),Interceptions VARCHAR(255),Positioning VARCHAR(255),Vision VARCHAR(255),Penalties VARCHAR(255),Composure VARCHAR(255),Marking VARCHAR(255),StandingTackle VARCHAR(255),SlidingTackle VARCHAR(255),GKDiving VARCHAR(255),GKHandling VARCHAR(255),GKKicking VARCHAR(255),GKPositioning VARCHAR(255),GKReflexes VARCHAR(255),ReleaseClause VARCHAR(255))"
    )
    cur.copy_from(f, 'players', sep=",")
    cur.execute("SELECT NAME FROM players")
    print(cur.fetchone())
    print(cur.fetchone())
    con.commit()

except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)

except IOError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()

    if f:
        f.close()
