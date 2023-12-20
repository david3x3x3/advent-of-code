import sys
from collections import defaultdict

lines = open(sys.argv[1]).read().strip().split('\n')

answer1 = 0

modules = defaultdict(dict)

for line in lines:
    parts = line.split(' -> ')
    if parts[0] == 'broadcaster':
        name = 'broadcaster'
    else:
        name = parts[0][1:]
    modules[name]['dest'] = parts[1].split(', ')
    modules[name]['in'] = []
    if name == 'broadcaster':
        modules[name]['type'] = '='
    else:
        modules[name]['type'] = parts[0][0]
    if modules[name]['type'] == '%':
        modules[name]['ff_on'] = False

    modules['rx']['in'] = []
    modules['rx']['dest'] = []
    modules['rx']['type'] = 'out'

    for name in modules:
        if modules[name]['type'] == '&':
            modules[name]['prev'] = {}
            for name2 in modules:
                if name in modules[name2]['dest']:
                    modules[name]['prev'][name2] = 'low'

if False:
    print('stateDiagram-v2')
    print('    [*] --> broadcaster')
    for name, module in modules.items():
        n = name
        if modules[name].get("type", "") == '&':
            n = "amp_" + name
        for name2 in module['dest']:
            n2 = name2
            #print(name, module, name2, modules[name2], flush=True)
            if modules[name2].get("type", "") == '&':
                n2 = "amp_" + name2
            print(f'    {n} --> {n2}')
    print('    rx --> [*]')
    sys.exit(0)
            
counts = {'low': 0, 'high': 0}
pushes = 0
while True:
    print(f'{pushes}:')
# 3877 3917 3769 3833
# 219388737656593
    for ids in ('qz,gc,xv,hq,zt,vl,bc,qx,gb,vj,hd,mg',
                'tx,jg,sb,lz,kk,vf,cn,tr,xz,lt,ng,gx',
                'jr,qm,bf,rr,cd,vn,lq,gk,kx,xg,pb,mt',
                'hk,tv,rl,qn,zr,vx,lj,fl,pp,zn,vh,cb'):
        print('  ', end='')
        num = 0
        for id in reversed(ids.split(',')):
            module = modules[id]
            num *= 2
            if module['type'] == '%':
                if module['ff_on']:
                    print(id, end=' ')
                    num += 1
                else:
                    print(id.upper(), end=' ')
        print(num)
    print([(amp, modules[amp]['prev'].values()) for amp in 'ks,pm,dl,vk'.split(',')])
    pushes += 1
    queue = ['broadcaster']
    #if pushes % 100000 == 0:
    if False:
        print(f'pushes = {pushes}')
    modules['broadcaster']['in'] = [('low', 'button')]
    # print(' sending low, button to broadcaster')
    counts['low'] += 1
    out_ = []
    while True:
        # done = True
        if len(queue) == 0:
            break
        id = queue.pop(0)
        module = modules[id]
        pulse, pulse_src = module['in'].pop(0)
        # for id, data in modules.items():
        #     if len(data['in']):
        #         done = False
        #         pulse, pulse_src = data['in'].pop(0)
        #         break
        # if done:
        #     break
        # print(f'processing {id} = {modules[id]}, pulse = {pulse}, {pulse_src}')
        if module['type'] == '=':
            for dest in module['dest']:
                # print(f' sending {pulse}, {id} to {dest}')
                counts[pulse] += 1
                modules[dest]['in'] += [(pulse, id)]
                queue += [dest]
        elif module['type'] == '%':
            if pulse == 'high':
                # ignore high pulse
                continue
            module['ff_on'] = not module['ff_on']
            for dest in module['dest']:
                if module['ff_on']:
                    # print(f' sending high, {id} to {dest}')
                    counts['high'] += 1
                    modules[dest]['in'] += [('high', id)]
                    queue += [dest]
                else:
                    # print(f' sending low, {id} to {dest}')
                    counts['low'] += 1
                    modules[dest]['in'] += [('low', id)]
                    queue += [dest]
        elif module['type'] == '&':
            # print(f' & received {pulse}')
            module['prev'][pulse_src] = pulse
            # print(f' prev = {module["prev"]}')
            if 'low' in module['prev'].values():
                p = 'high'
            else:
                p = 'low'
            for dest in module['dest']:
                # print(f' sending {p}, {id} to {dest}')
                counts[p] += 1
                modules[dest]['in'] += [(p, id)]
                queue += [dest]
        elif module['type'] == 'out':
            out_ += [(pulse, pulse_src)]
    # print(f'result = {out_}')
    while len(out_):
        if out_.pop()[0] == 'low':
            break
#print(f'low = {counts["low"]}, high = {counts["high"]}, answer1 = {counts["low"]*counts["high"]}')
print(f'answer = {pushes}')
# print(out_)
