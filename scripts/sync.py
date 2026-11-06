"""Merge existing public distribution sources; no credentials or private repos."""
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    'https://raw.githubusercontent.com/atsrxL/scatter-altstore/main/altstore/source.json',
    'https://raw.githubusercontent.com/atsrxL/sendit/main/altstore/source.json',
    'https://raw.githubusercontent.com/atsrxL/F50Manager-iOS/main/altstore.json',
    'https://github.com/atsrxL/FlowStream/releases/download/ios-latest/source.json',
]


def main():
    apps = []
    identifiers = set()
    for url in SOURCES:
        request = urllib.request.Request(url, headers={'User-Agent': 'atsrxl-alt-repo'})
        with urllib.request.urlopen(request, timeout=60) as response:
            source = json.load(response)
        for app in source['apps']:
            identifier = app['bundleIdentifier']
            if identifier in identifiers:
                raise ValueError(f'Duplicate app: {identifier}')
            identifiers.add(identifier)
            if not app.get('versions'):
                raise ValueError(f'Missing versions: {identifier}')
            latest = app['versions'][0]
            for version in app['versions']:
                if not version['downloadURL'].startswith('https://') or version['size'] <= 0:
                    raise ValueError(f'Invalid release: {identifier}')
            # Also expose legacy fields used by some signing clients.
            app.update(version=latest['version'], versionDate=latest['date'],
                       versionDescription=latest.get('localizedDescription', ''),
                       downloadURL=latest['downloadURL'], size=latest['size'])
            apps.append(app)
    output = {
        'name': 'atsrxL Apps',
        'identifier': 'com.atsrxl.altrepo',
        'subtitle': '个人 iOS / iPadOS 应用合集',
        'description': 'Scatter、SendIt、F50 Manager 与映流 FlowStream 的统一公开分发源。',
        'website': 'https://github.com/atsrxL/alt-repo',
        'iconURL': 'https://raw.githubusercontent.com/atsrxL/scatter-altstore/main/altstore/icon.png',
        'tintColor': '7564CF',
        'apps': apps,
        'news': [],
    }
    # Write only after every upstream source succeeds.
    (ROOT / 'source.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print('Updated source.json: ' + ', '.join(a['name'] + ' ' + a['version'] for a in apps))


if __name__ == '__main__':
    main()
