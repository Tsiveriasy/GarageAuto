from django.core.management.base import BaseCommand
from garage.models import Service

class Command(BaseCommand):
    help = 'Adds default services to the database'

    def handle(self, *args, **kwargs):
        services = [
            {
                'name': 'Révision générale',
                'description': 'Inspection complète de votre véhicule pour assurer sa performance et sa sécurité.',
                'price': 600000,
                'icon': 'clipboard-check'
            },
            {
                'name': 'Changement d\'huile',
                'description': 'Remplacement de l\'huile moteur et du filtre pour maintenir les performances du moteur.',
                'price': 320000,
                'icon': 'beaker'
            },
            {
                'name': 'Freins',
                'description': 'Inspection et remplacement des plaquettes, disques ou tambours de frein si nécessaire.',
                'price': 800000,
                'icon': 'hand'
            },
            {
                'name': 'Suspension',
                'description': 'Vérification et réparation des composants de la suspension pour un meilleur confort de conduite.',
                'price': 1000000,
                'icon': 'arrows-up-down'
            },
            {
                'name': 'Diagnostic électronique',
                'description': 'Analyse complète des systèmes électroniques de votre véhicule.',
                'price': 400000,
                'icon': 'cpu-chip'
            },
            {
                'name': 'Climatisation',
                'description': 'Entretien et recharge du système de climatisation.',
                'price': 480000,
                'icon': 'sun'
            },
            {
                'name': 'Pneus',
                'description': 'Remplacement, équilibrage et permutation des pneus.',
                'price': 1120000,
                'icon': 'circle-stack'
            },
            {
                'name': 'Batterie',
                'description': 'Test et remplacement de la batterie si nécessaire.',
                'price': 600000,
                'icon': 'battery-100'
            },
            {
                'name': 'Échappement',
                'description': 'Inspection et réparation du système d\'échappement.',
                'price': 720000,
                'icon': 'arrow-up-circle'
            },
            {
                'name': 'Courroie de distribution',
                'description': 'Remplacement de la courroie de distribution et des composants associés.',
                'price': 2000000,
                'icon': 'cog'
            },
        ]

        for service_data in services:
            Service.objects.get_or_create(
                name=service_data['name'],
                defaults={
                    'description': service_data['description'],
                    'price': service_data['price'],
                    'icon': service_data['icon']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added default services'))

