#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on June 20, 2024, at 17:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
expName = 'AB'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'order': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\TuebingenLab\\Desktop\\code\\Luck1996AB-newversion0422_2\\AB 0422.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instructions" ---
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from code_instr
# open file with instructions
with open('instruction.txt', 'r') as file:
    text = file.read()

# add the text in the variable
text_instructions.text = text
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "settings" ---
# Run 'Begin Experiment' code from code
import random

related_idx = list(range(360))
unrelated_idx = list(range(360,720))
random.shuffle(related_idx)
random.shuffle(unrelated_idx)


# --- Initialize components for Routine "T0_context" ---
context_word = visual.TextStim(win=win, name='context_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blankContext = visual.TextStim(win=win, name='blankContext',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "distractors_T0_T2" ---
text_distractors_2 = visual.TextStim(win=win, name='text_distractors_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "T1_number" ---
text_T1 = visual.TextStim(win=win, name='text_T1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "distractors_T1" ---
text_distractors = visual.TextStim(win=win, name='text_distractors',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "T2_probe" ---
text_T2 = visual.TextStim(win=win, name='text_T2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "distractors_T0_T2" ---
text_distractors_2 = visual.TextStim(win=win, name='text_distractors_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Ask_T1" ---
blankT1_1 = visual.TextStim(win=win, name='blankT1_1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_T1ask = visual.TextStim(win=win, name='text_T1ask',
    text='?\n\nOdd-F    Even-J',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
blankT1_2 = visual.TextStim(win=win, name='blankT1_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_T1 = keyboard.Keyboard()

# --- Initialize components for Routine "Ask_T2" ---
blankT2_1 = visual.TextStim(win=win, name='blankT2_1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_T2ask = visual.TextStim(win=win, name='text_T2ask',
    text='?\n\nRelated-F    Unrelated-J',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
blankT2_2 = visual.TextStim(win=win, name='blankT2_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_T2 = keyboard.Keyboard()

# --- Initialize components for Routine "rest" ---
text = visual.TextStim(win=win, name='text',
    text='rest',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [text_instructions, key_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions* updates
    
    # if text_instructions is starting this frame...
    if text_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.tStart = t  # local t and not account for scr refresh
        text_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_instructions.started')
        # update status
        text_instructions.status = STARTED
        text_instructions.setAutoDraw(True)
    
    # if text_instructions is active this frame...
    if text_instructions.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
taskType_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task_type.xlsx'),
    seed=None, name='taskType_loop')
thisExp.addLoop(taskType_loop)  # add the loop to the experiment
thisTaskType_loop = taskType_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTaskType_loop.rgb)
if thisTaskType_loop != None:
    for paramName in thisTaskType_loop:
        exec('{} = thisTaskType_loop[paramName]'.format(paramName))

for thisTaskType_loop in taskType_loop:
    currentLoop = taskType_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTaskType_loop.rgb)
    if thisTaskType_loop != None:
        for paramName in thisTaskType_loop:
            exec('{} = thisTaskType_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "settings" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    task = task1 if expInfo['order']=='1' else task2
    n = 30
    trials_in_block = related_idx[-n:] + unrelated_idx[-n:]
    shuffle(trials_in_block)
    related_idx = related_idx[:len(related_idx)-n]
    unrelated_idx = unrelated_idx[:len(unrelated_idx)-n]
    
    # keep track of which components have finished
    settingsComponents = []
    for thisComponent in settingsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "settings" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in settingsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "settings" ---
    for thisComponent in settingsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    block = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('wordPairs.xlsx', selection=trials_in_block),
        seed=None, name='block')
    thisExp.addLoop(block)  # add the loop to the experiment
    thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in block:
        currentLoop = block
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "T0_context" ---
        continueRoutine = True
        # update component parameters for each repeat
        context_word.setText(T0)
        # keep track of which components have finished
        T0_contextComponents = [context_word, blankContext]
        for thisComponent in T0_contextComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "T0_context" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *context_word* updates
            
            # if context_word is starting this frame...
            if context_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                context_word.frameNStart = frameN  # exact frame index
                context_word.tStart = t  # local t and not account for scr refresh
                context_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(context_word, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'context_word.started')
                # update status
                context_word.status = STARTED
                context_word.setAutoDraw(True)
            
            # if context_word is active this frame...
            if context_word.status == STARTED:
                # update params
                pass
            
            # if context_word is stopping this frame...
            if context_word.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > context_word.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    context_word.tStop = t  # not accounting for scr refresh
                    context_word.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'context_word.stopped')
                    # update status
                    context_word.status = FINISHED
                    context_word.setAutoDraw(False)
            
            # *blankContext* updates
            
            # if blankContext is starting this frame...
            if blankContext.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                blankContext.frameNStart = frameN  # exact frame index
                blankContext.tStart = t  # local t and not account for scr refresh
                blankContext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankContext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankContext.started')
                # update status
                blankContext.status = STARTED
                blankContext.setAutoDraw(True)
            
            # if blankContext is active this frame...
            if blankContext.status == STARTED:
                # update params
                pass
            
            # if blankContext is stopping this frame...
            if blankContext.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankContext.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blankContext.tStop = t  # not accounting for scr refresh
                    blankContext.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blankContext.stopped')
                    # update status
                    blankContext.status = FINISHED
                    blankContext.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T0_contextComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T0_context" ---
        for thisComponent in T0_contextComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        trials_T0_context = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('distractors.csv', selection="0:{}".format(lagT0-1)),
            seed=None, name='trials_T0_context')
        thisExp.addLoop(trials_T0_context)  # add the loop to the experiment
        thisTrials_T0_context = trials_T0_context.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_T0_context.rgb)
        if thisTrials_T0_context != None:
            for paramName in thisTrials_T0_context:
                exec('{} = thisTrials_T0_context[paramName]'.format(paramName))
        
        for thisTrials_T0_context in trials_T0_context:
            currentLoop = trials_T0_context
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_T0_context.rgb)
            if thisTrials_T0_context != None:
                for paramName in thisTrials_T0_context:
                    exec('{} = thisTrials_T0_context[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "distractors_T0_T2" ---
            continueRoutine = True
            # update component parameters for each repeat
            text_distractors_2.setText(dist)
            # keep track of which components have finished
            distractors_T0_T2Components = [text_distractors_2]
            for thisComponent in distractors_T0_T2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "distractors_T0_T2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.083:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_distractors_2* updates
                
                # if text_distractors_2 is starting this frame...
                if text_distractors_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    text_distractors_2.frameNStart = frameN  # exact frame index
                    text_distractors_2.tStart = t  # local t and not account for scr refresh
                    text_distractors_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_distractors_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_distractors_2.started')
                    # update status
                    text_distractors_2.status = STARTED
                    text_distractors_2.setAutoDraw(True)
                
                # if text_distractors_2 is active this frame...
                if text_distractors_2.status == STARTED:
                    # update params
                    pass
                
                # if text_distractors_2 is stopping this frame...
                if text_distractors_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_distractors_2.tStartRefresh + 0.083-frameTolerance:
                        # keep track of stop time/frame for later
                        text_distractors_2.tStop = t  # not accounting for scr refresh
                        text_distractors_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_distractors_2.stopped')
                        # update status
                        text_distractors_2.status = FINISHED
                        text_distractors_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in distractors_T0_T2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "distractors_T0_T2" ---
            for thisComponent in distractors_T0_T2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.083000)
        # completed 1.0 repeats of 'trials_T0_context'
        
        
        # --- Prepare to start Routine "T1_number" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_T1.setText('{:07}'.format(T1))
        # keep track of which components have finished
        T1_numberComponents = [text_T1]
        for thisComponent in T1_numberComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "T1_number" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.083:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_T1* updates
            
            # if text_T1 is starting this frame...
            if text_T1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_T1.frameNStart = frameN  # exact frame index
                text_T1.tStart = t  # local t and not account for scr refresh
                text_T1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_T1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_T1.started')
                # update status
                text_T1.status = STARTED
                text_T1.setAutoDraw(True)
            
            # if text_T1 is active this frame...
            if text_T1.status == STARTED:
                # update params
                pass
            
            # if text_T1 is stopping this frame...
            if text_T1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_T1.tStartRefresh + 0.083-frameTolerance:
                    # keep track of stop time/frame for later
                    text_T1.tStop = t  # not accounting for scr refresh
                    text_T1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_T1.stopped')
                    # update status
                    text_T1.status = FINISHED
                    text_T1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1_numberComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1_number" ---
        for thisComponent in T1_numberComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.083000)
        
        # set up handler to look after randomisation of conditions etc
        trials_T1 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('distractors.csv', selection="0:{}".format(lagT1-1)),
            seed=None, name='trials_T1')
        thisExp.addLoop(trials_T1)  # add the loop to the experiment
        thisTrials_T1 = trials_T1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_T1.rgb)
        if thisTrials_T1 != None:
            for paramName in thisTrials_T1:
                exec('{} = thisTrials_T1[paramName]'.format(paramName))
        
        for thisTrials_T1 in trials_T1:
            currentLoop = trials_T1
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_T1.rgb)
            if thisTrials_T1 != None:
                for paramName in thisTrials_T1:
                    exec('{} = thisTrials_T1[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "distractors_T1" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from skipLoop_ifLag1
            if lagT1==1:
                 continueRoutine = False
            text_distractors.setText(dist)
            # keep track of which components have finished
            distractors_T1Components = [text_distractors]
            for thisComponent in distractors_T1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "distractors_T1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.083:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_distractors* updates
                
                # if text_distractors is starting this frame...
                if text_distractors.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    text_distractors.frameNStart = frameN  # exact frame index
                    text_distractors.tStart = t  # local t and not account for scr refresh
                    text_distractors.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_distractors, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_distractors.started')
                    # update status
                    text_distractors.status = STARTED
                    text_distractors.setAutoDraw(True)
                
                # if text_distractors is active this frame...
                if text_distractors.status == STARTED:
                    # update params
                    pass
                
                # if text_distractors is stopping this frame...
                if text_distractors.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_distractors.tStartRefresh + 0.083-frameTolerance:
                        # keep track of stop time/frame for later
                        text_distractors.tStop = t  # not accounting for scr refresh
                        text_distractors.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_distractors.stopped')
                        # update status
                        text_distractors.status = FINISHED
                        text_distractors.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in distractors_T1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "distractors_T1" ---
            for thisComponent in distractors_T1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.083000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_T1'
        
        
        # --- Prepare to start Routine "T2_probe" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_T2.setText(T2)
        # keep track of which components have finished
        T2_probeComponents = [text_T2]
        for thisComponent in T2_probeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "T2_probe" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.083:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_T2* updates
            
            # if text_T2 is starting this frame...
            if text_T2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_T2.frameNStart = frameN  # exact frame index
                text_T2.tStart = t  # local t and not account for scr refresh
                text_T2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_T2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_T2.started')
                # update status
                text_T2.status = STARTED
                text_T2.setAutoDraw(True)
            
            # if text_T2 is active this frame...
            if text_T2.status == STARTED:
                # update params
                pass
            
            # if text_T2 is stopping this frame...
            if text_T2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_T2.tStartRefresh + 0.083-frameTolerance:
                    # keep track of stop time/frame for later
                    text_T2.tStop = t  # not accounting for scr refresh
                    text_T2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_T2.stopped')
                    # update status
                    text_T2.status = FINISHED
                    text_T2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2_probeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2_probe" ---
        for thisComponent in T2_probeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.083000)
        
        # set up handler to look after randomisation of conditions etc
        trials_T2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('distractors.csv', selection="0:{}".format(lagT2)),
            seed=None, name='trials_T2')
        thisExp.addLoop(trials_T2)  # add the loop to the experiment
        thisTrials_T2 = trials_T2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_T2.rgb)
        if thisTrials_T2 != None:
            for paramName in thisTrials_T2:
                exec('{} = thisTrials_T2[paramName]'.format(paramName))
        
        for thisTrials_T2 in trials_T2:
            currentLoop = trials_T2
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_T2.rgb)
            if thisTrials_T2 != None:
                for paramName in thisTrials_T2:
                    exec('{} = thisTrials_T2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "distractors_T0_T2" ---
            continueRoutine = True
            # update component parameters for each repeat
            text_distractors_2.setText(dist)
            # keep track of which components have finished
            distractors_T0_T2Components = [text_distractors_2]
            for thisComponent in distractors_T0_T2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "distractors_T0_T2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.083:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_distractors_2* updates
                
                # if text_distractors_2 is starting this frame...
                if text_distractors_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    text_distractors_2.frameNStart = frameN  # exact frame index
                    text_distractors_2.tStart = t  # local t and not account for scr refresh
                    text_distractors_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_distractors_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_distractors_2.started')
                    # update status
                    text_distractors_2.status = STARTED
                    text_distractors_2.setAutoDraw(True)
                
                # if text_distractors_2 is active this frame...
                if text_distractors_2.status == STARTED:
                    # update params
                    pass
                
                # if text_distractors_2 is stopping this frame...
                if text_distractors_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_distractors_2.tStartRefresh + 0.083-frameTolerance:
                        # keep track of stop time/frame for later
                        text_distractors_2.tStop = t  # not accounting for scr refresh
                        text_distractors_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_distractors_2.stopped')
                        # update status
                        text_distractors_2.status = FINISHED
                        text_distractors_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                    if eyetracker:
                        eyetracker.setConnectionState(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in distractors_T0_T2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "distractors_T0_T2" ---
            for thisComponent in distractors_T0_T2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.083000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_T2'
        
        
        # --- Prepare to start Routine "Ask_T1" ---
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_T1.keys = []
        key_resp_T1.rt = []
        _key_resp_T1_allKeys = []
        # Run 'Begin Routine' code from code_2
        if task == 'single':
            continueRoutine = False
        # keep track of which components have finished
        Ask_T1Components = [blankT1_1, text_T1ask, blankT1_2, key_resp_T1]
        for thisComponent in Ask_T1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Ask_T1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blankT1_1* updates
            
            # if blankT1_1 is starting this frame...
            if blankT1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blankT1_1.frameNStart = frameN  # exact frame index
                blankT1_1.tStart = t  # local t and not account for scr refresh
                blankT1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankT1_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankT1_1.started')
                # update status
                blankT1_1.status = STARTED
                blankT1_1.setAutoDraw(True)
            
            # if blankT1_1 is active this frame...
            if blankT1_1.status == STARTED:
                # update params
                pass
            
            # if blankT1_1 is stopping this frame...
            if blankT1_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankT1_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blankT1_1.tStop = t  # not accounting for scr refresh
                    blankT1_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blankT1_1.stopped')
                    # update status
                    blankT1_1.status = FINISHED
                    blankT1_1.setAutoDraw(False)
            
            # *text_T1ask* updates
            
            # if text_T1ask is starting this frame...
            if text_T1ask.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                text_T1ask.frameNStart = frameN  # exact frame index
                text_T1ask.tStart = t  # local t and not account for scr refresh
                text_T1ask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_T1ask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_T1ask.started')
                # update status
                text_T1ask.status = STARTED
                text_T1ask.setAutoDraw(True)
            
            # if text_T1ask is active this frame...
            if text_T1ask.status == STARTED:
                # update params
                pass
            
            # if text_T1ask is stopping this frame...
            if text_T1ask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_T1ask.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_T1ask.tStop = t  # not accounting for scr refresh
                    text_T1ask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_T1ask.stopped')
                    # update status
                    text_T1ask.status = FINISHED
                    text_T1ask.setAutoDraw(False)
            
            # *blankT1_2* updates
            
            # if blankT1_2 is starting this frame...
            if blankT1_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                blankT1_2.frameNStart = frameN  # exact frame index
                blankT1_2.tStart = t  # local t and not account for scr refresh
                blankT1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankT1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankT1_2.started')
                # update status
                blankT1_2.status = STARTED
                blankT1_2.setAutoDraw(True)
            
            # if blankT1_2 is active this frame...
            if blankT1_2.status == STARTED:
                # update params
                pass
            
            # if blankT1_2 is stopping this frame...
            if blankT1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankT1_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blankT1_2.tStop = t  # not accounting for scr refresh
                    blankT1_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blankT1_2.stopped')
                    # update status
                    blankT1_2.status = FINISHED
                    blankT1_2.setAutoDraw(False)
            
            # *key_resp_T1* updates
            waitOnFlip = False
            
            # if key_resp_T1 is starting this frame...
            if key_resp_T1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_T1.frameNStart = frameN  # exact frame index
                key_resp_T1.tStart = t  # local t and not account for scr refresh
                key_resp_T1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_T1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_T1.started')
                # update status
                key_resp_T1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_T1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_T1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_T1 is stopping this frame...
            if key_resp_T1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_T1.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_T1.tStop = t  # not accounting for scr refresh
                    key_resp_T1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_T1.stopped')
                    # update status
                    key_resp_T1.status = FINISHED
                    key_resp_T1.status = FINISHED
            if key_resp_T1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_T1.getKeys(keyList=['f','j'], waitRelease=False)
                _key_resp_T1_allKeys.extend(theseKeys)
                if len(_key_resp_T1_allKeys):
                    key_resp_T1.keys = _key_resp_T1_allKeys[-1].name  # just the last key pressed
                    key_resp_T1.rt = _key_resp_T1_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_T1.keys == str(responseT1)) or (key_resp_T1.keys == responseT1):
                        key_resp_T1.corr = 1
                    else:
                        key_resp_T1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Ask_T1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Ask_T1" ---
        for thisComponent in Ask_T1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_T1.keys in ['', [], None]:  # No response was made
            key_resp_T1.keys = None
            # was no response the correct answer?!
            if str(responseT1).lower() == 'none':
               key_resp_T1.corr = 1;  # correct non-response
            else:
               key_resp_T1.corr = 0;  # failed to respond (incorrectly)
        # store data for block (TrialHandler)
        block.addData('key_resp_T1.keys',key_resp_T1.keys)
        block.addData('key_resp_T1.corr', key_resp_T1.corr)
        if key_resp_T1.keys != None:  # we had a response
            block.addData('key_resp_T1.rt', key_resp_T1.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "Ask_T2" ---
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_T2.keys = []
        key_resp_T2.rt = []
        _key_resp_T2_allKeys = []
        # keep track of which components have finished
        Ask_T2Components = [blankT2_1, text_T2ask, blankT2_2, key_resp_T2]
        for thisComponent in Ask_T2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Ask_T2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blankT2_1* updates
            
            # if blankT2_1 is starting this frame...
            if blankT2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blankT2_1.frameNStart = frameN  # exact frame index
                blankT2_1.tStart = t  # local t and not account for scr refresh
                blankT2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankT2_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankT2_1.started')
                # update status
                blankT2_1.status = STARTED
                blankT2_1.setAutoDraw(True)
            
            # if blankT2_1 is active this frame...
            if blankT2_1.status == STARTED:
                # update params
                pass
            
            # if blankT2_1 is stopping this frame...
            if blankT2_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankT2_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blankT2_1.tStop = t  # not accounting for scr refresh
                    blankT2_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blankT2_1.stopped')
                    # update status
                    blankT2_1.status = FINISHED
                    blankT2_1.setAutoDraw(False)
            
            # *text_T2ask* updates
            
            # if text_T2ask is starting this frame...
            if text_T2ask.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                text_T2ask.frameNStart = frameN  # exact frame index
                text_T2ask.tStart = t  # local t and not account for scr refresh
                text_T2ask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_T2ask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_T2ask.started')
                # update status
                text_T2ask.status = STARTED
                text_T2ask.setAutoDraw(True)
            
            # if text_T2ask is active this frame...
            if text_T2ask.status == STARTED:
                # update params
                pass
            
            # if text_T2ask is stopping this frame...
            if text_T2ask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_T2ask.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_T2ask.tStop = t  # not accounting for scr refresh
                    text_T2ask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_T2ask.stopped')
                    # update status
                    text_T2ask.status = FINISHED
                    text_T2ask.setAutoDraw(False)
            
            # *blankT2_2* updates
            
            # if blankT2_2 is starting this frame...
            if blankT2_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                blankT2_2.frameNStart = frameN  # exact frame index
                blankT2_2.tStart = t  # local t and not account for scr refresh
                blankT2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankT2_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blankT2_2.started')
                # update status
                blankT2_2.status = STARTED
                blankT2_2.setAutoDraw(True)
            
            # if blankT2_2 is active this frame...
            if blankT2_2.status == STARTED:
                # update params
                pass
            
            # if blankT2_2 is stopping this frame...
            if blankT2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankT2_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blankT2_2.tStop = t  # not accounting for scr refresh
                    blankT2_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blankT2_2.stopped')
                    # update status
                    blankT2_2.status = FINISHED
                    blankT2_2.setAutoDraw(False)
            
            # *key_resp_T2* updates
            waitOnFlip = False
            
            # if key_resp_T2 is starting this frame...
            if key_resp_T2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_T2.frameNStart = frameN  # exact frame index
                key_resp_T2.tStart = t  # local t and not account for scr refresh
                key_resp_T2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_T2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_T2.started')
                # update status
                key_resp_T2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_T2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_T2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_T2 is stopping this frame...
            if key_resp_T2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_T2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_T2.tStop = t  # not accounting for scr refresh
                    key_resp_T2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_T2.stopped')
                    # update status
                    key_resp_T2.status = FINISHED
                    key_resp_T2.status = FINISHED
            if key_resp_T2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_T2.getKeys(keyList=['f','j'], waitRelease=False)
                _key_resp_T2_allKeys.extend(theseKeys)
                if len(_key_resp_T2_allKeys):
                    key_resp_T2.keys = _key_resp_T2_allKeys[-1].name  # just the last key pressed
                    key_resp_T2.rt = _key_resp_T2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_T2.keys == str(responseT2)) or (key_resp_T2.keys == responseT2):
                        key_resp_T2.corr = 1
                    else:
                        key_resp_T2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Ask_T2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Ask_T2" ---
        for thisComponent in Ask_T2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_T2.keys in ['', [], None]:  # No response was made
            key_resp_T2.keys = None
            # was no response the correct answer?!
            if str(responseT2).lower() == 'none':
               key_resp_T2.corr = 1;  # correct non-response
            else:
               key_resp_T2.corr = 0;  # failed to respond (incorrectly)
        # store data for block (TrialHandler)
        block.addData('key_resp_T2.keys',key_resp_T2.keys)
        block.addData('key_resp_T2.corr', key_resp_T2.corr)
        if key_resp_T2.keys != None:  # we had a response
            block.addData('key_resp_T2.rt', key_resp_T2.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block'
    
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    restComponents = [text]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'taskType_loop'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
